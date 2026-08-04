def prism_detector(grid: list[str], pattern: str) -> list[tuple[int, int, str]]:
    if not grid or not pattern:
        return []

    dirs = [(0, 1, "H"), (0, -1, "H-"), (1, 0, "V"), (-1, 0, "V-"),
            (1, 1, "D1"), (-1, -1, "D1-"), (1, -1, "D2"), (-1, 1, "D2-")]

    rows, res = len(grid), []
    for r in range(rows):
        for c in range(len(grid[r])):
            for dr, dc, code in dirs:
                for k, ch in enumerate(pattern):
                    rr, cc = r + dr * k, c + dc * k
                    if not (0 <= rr < rows and 0 <= cc < len(grid[rr])) or grid[rr][cc] != ch:
                        break
                else:
                    res.append((r, c, code))
    return res
