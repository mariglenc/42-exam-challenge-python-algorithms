"""Import an attempt file, find the target function, run it against examples.

The attempt is loaded straight from its file path (importlib) under a unique,
throwaway module name, so the folder name (``ex2-1``) and repeated grading in
one process never clash. The exercise folder is briefly put on ``sys.path`` in
case the attempt imports a helper next to it.

Grading is a plain ``==`` comparison with ONE deliberate exception: ``bool`` is
a subclass of ``int`` in Python, so ``True == 1`` is otherwise True. We keep
bools and ints distinct at the top level, so returning ``1`` when ``True`` is
expected is graded as a FAIL (these exercises really do mean the bool).

Each example runs in a separate child process with a time limit (default 5s,
override with ``STUDYTOOL_TIMEOUT``). An attempt stuck in an infinite loop is
killed and scored as TIMEOUT instead of hanging the grader and eating RAM.
"""
from __future__ import annotations

import contextlib
import importlib.util
import io
import multiprocessing as mp
import os
import sys
import traceback
from dataclasses import dataclass, field
from typing import Any, Callable

from .enparser import Example, ParsedEn

_load_counter = 0

DEFAULT_TIMEOUT = 5.0

# fork (Linux/macOS) starts children in milliseconds; Windows only has spawn
_CTX = mp.get_context("fork" if "fork" in mp.get_all_start_methods() else "spawn")


@dataclass
class ExampleResult:
    call: str
    status: str                 # 'PASS' | 'FAIL' | 'ERROR' | 'SKIP'
    expected: Any = None
    got: Any = None
    detail: str = ""            # error text, or skip reason


@dataclass
class GradeResult:
    ex_id: str
    try_file: str               # basename, e.g. 'try2.py'
    results: list[ExampleResult] = field(default_factory=list)
    passed: int = 0
    gradeable: int = 0          # examples we could actually check
    skipped: int = 0            # examples with a cut-off/unparseable side
    load_error: str | None = None

    @property
    def total_examples(self) -> int:
        return len(self.results)

    @property
    def score(self) -> float:
        """Fraction of *gradeable* examples that passed (0.0 if none)."""
        return self.passed / self.gradeable if self.gradeable else 0.0

    @property
    def all_passed(self) -> bool:
        """True only if there was something to grade and everything passed."""
        return self.gradeable > 0 and self.passed == self.gradeable and not self.load_error


def _values_equal(got: Any, expected: Any) -> bool:
    """Equality that keeps bool distinct from int at the top level."""
    if isinstance(expected, bool) or isinstance(got, bool):
        return isinstance(got, bool) and isinstance(expected, bool) and got == expected
    return got == expected


def _load_function(try_path: str, func_name: str | None) -> Callable:
    """Import the attempt and return its target callable.

    Prefers a function literally named ``func_name``; if that's missing, falls
    back to the sole top-level function defined in the module. Raises with a
    clear message otherwise. stdout produced at import time is swallowed.
    """
    global _load_counter
    _load_counter += 1
    mod_name = f"_studytool_attempt_{_load_counter}"

    spec = importlib.util.spec_from_file_location(mod_name, try_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"cannot load {try_path}")
    module = importlib.util.module_from_spec(spec)

    ex_dir = os.path.dirname(try_path)
    sys.path.insert(0, ex_dir)
    sys.modules[mod_name] = module
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(module)
    finally:
        sys.path.remove(ex_dir)
        sys.modules.pop(mod_name, None)

    func = getattr(module, func_name, None) if func_name else None
    if callable(func):
        return func

    # fallback: exactly one function *defined in this module*
    defined = [
        v for v in vars(module).values()
        if callable(v) and getattr(v, "__module__", None) == mod_name
    ]
    if len(defined) == 1:
        return defined[0]
    if not defined:
        raise AttributeError(f"no function named {func_name!r} found in {os.path.basename(try_path)}")
    raise AttributeError(
        f"{func_name!r} not found and {len(defined)} functions are defined "
        f"in {os.path.basename(try_path)} (can't tell which to grade)"
    )


def _example_worker(conn, try_path: str, func_name: str | None, args, kwargs) -> None:
    """Child-process body: load the attempt, run one example, send the outcome.

    Runs in a separate process so the parent can kill it if the attempt never
    returns (infinite loop) or allocates unboundedly.
    """
    try:
        func = _load_function(try_path, func_name)
    except Exception as exc:  # noqa: BLE001 - report any import/load failure verbatim
        conn.send(("load_error", f"{type(exc).__name__}: {exc}"))
        return
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            got = func(*args, **kwargs)
    except Exception as exc:  # noqa: BLE001 - the attempt raised; that's a failing case
        conn.send(("error", f"{type(exc).__name__}: {exc}"))
        return
    try:
        conn.send(("ok", got))
    except Exception as exc:  # noqa: BLE001 - e.g. return value not picklable
        conn.send(("error", f"return value could not be sent back: {exc}"))


def _run_example(try_path: str, func_name: str | None, ex: Example,
                 timeout: float) -> tuple[str, Any]:
    """Run one example in a child process; kill it after ``timeout`` seconds."""
    parent_conn, child_conn = _CTX.Pipe(duplex=False)
    proc = _CTX.Process(
        target=_example_worker,
        args=(child_conn, try_path, func_name, ex.args, ex.kwargs),
        daemon=True,
    )
    proc.start()
    child_conn.close()
    try:
        if parent_conn.poll(timeout):
            try:
                kind, payload = parent_conn.recv()
            except EOFError:  # child died without reporting (crash, exit())
                kind, payload = "error", "attempt process died unexpectedly"
        else:
            kind, payload = "timeout", (
                f"no result after {timeout:g}s - killed (likely an infinite loop)"
            )
    finally:
        if proc.is_alive():
            proc.kill()
        proc.join()
        parent_conn.close()
    return kind, payload


def grade_file(parsed: ParsedEn, try_path: str, ex_id: str,
               timeout: float | None = None) -> GradeResult:
    """Run every gradeable example from ``parsed`` against ``try_path``."""
    if timeout is None:
        timeout = float(os.environ.get("STUDYTOOL_TIMEOUT", DEFAULT_TIMEOUT))
    res = GradeResult(ex_id=ex_id, try_file=os.path.basename(try_path))

    for ex in parsed.examples:
        if not ex.gradeable:
            reason = ex.note or "example not fully parseable"
            res.results.append(ExampleResult(call=ex.call, status="SKIP", detail=reason))
            res.skipped += 1
            continue

        res.gradeable += 1
        kind, got = _run_example(try_path, parsed.func_name, ex, timeout)

        if kind == "load_error":
            res.load_error = got
            return res
        if kind == "timeout":
            res.results.append(ExampleResult(
                call=ex.call, status="TIMEOUT", expected=ex.expected, detail=got))
            continue
        if kind == "error":
            res.results.append(ExampleResult(
                call=ex.call, status="ERROR", expected=ex.expected, detail=got))
            continue

        if _values_equal(got, ex.expected):
            res.passed += 1
            res.results.append(ExampleResult(
                call=ex.call, status="PASS", expected=ex.expected, got=got))
        else:
            res.results.append(ExampleResult(
                call=ex.call, status="FAIL", expected=ex.expected, got=got))

    return res


# Kept for symmetry / possible reuse; the CLI formats results itself.
def format_traceback(exc: BaseException) -> str:
    return "".join(traceback.format_exception(type(exc), exc, exc.__traceback__))
