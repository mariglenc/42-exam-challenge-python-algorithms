class DependencyResolver:
    def __init__(self, deps):
        self.deps = deps
        self.visited = set()
        self.visiting = set()
        self.order = []

    def resolve(self):
        for pkg in self.deps:
            if pkg not in self.visited:
                self._dfs(pkg)
        return self.order[::-1]

    def _dfs(self, pkg):
        if pkg in self.visiting: # check if is already in visiting sets
            raise ValueError(f"Cyclic dependency detected involving '{pkg}'") # if so throw error

        if pkg in self.visited: # check if already visited sets
            return # if so return stop here dont continue down

        self.visiting.add(pkg) # add in visiting set

        for dep in self.deps.get(pkg, []): # for each thing this package depends on
            self._dfs(dep) # call _dfs on it

        self.visiting.remove(pkg)   # remove an item from the set because no longer exploring this 
        self.visited.add(pkg)       # add an item to the set because this is now finished
        self.order.append(pkg)      # add pkg to the end of the list

def resolve_dependencies(deps: dict[str, list[str]]) -> list[str]:
    return DependencyResolver(deps).resolve()


print(resolve_dependencies({'app': ['lib1', 'lib2'], 'lib1': ['core'], 'lib2': ['core'], 'core': []}))  # ['app', 'lib2', 'lib1', 'core']
print(resolve_dependencies({'a': ['b'], 'b': ['c'], 'c': []}))                                          # ['a', 'b', 'c']
print(resolve_dependencies({'a': []}))                                                                  # ['a']
