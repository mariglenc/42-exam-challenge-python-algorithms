# ex4-2 - resolve_dependencies
# attempt: try4.py
# (signature pre-filled from the .en; write your solution below)
class DependencieResolver:
    def __init__(self,deps):
        self.deps=deps
        self.visiting=set()
        self.visited=set()
        self.order=[]

    def resolve(self):
        for pkg in self.deps:
            if pkg not in self.visited:
                self._dfs(pkg)

        return self.order[::-1]

    def _dfs(self,pkg): # why we pass pkg here in params, cant we use self.pkg or sth like self.deps.get(pkg,[] ) maybe ??
        if pkg in self.visiting:
            raise ValueError("already visiting")
        if pkg in self.visited:
            return
        self.visiting.add(pkg)
        for dep in self.deps.get(pkg,[]):
            self._dfs(dep)
        self.visiting.remove(pkg)
        self.visited.add(pkg)
        self.order.append(pkg)

def resolve_dependencies(deps: dict[str, list[str]]) -> list[str]:
    return DependencieResolver(deps).resolve()