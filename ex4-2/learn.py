
class DependencyResolver:

    def __init__(self,deps):
        self.deps=deps
        self.visited=set()
        self.visiting=set()
        self.order=[]
    # declare constuctor:
        # self.deps=deps
        # self.visited=set()
        # self.visiting=set()
        # self.order=[]
    
    def resolve(self):
        for pkg in self.deps:
            if pkg not in self.visited:
                self._dfs(pkg)
        return self.order[::-1]

    # decalre resolve with self paramter -> at the main function we execute the resolve
        # iterate over all self.deps
        # if not in self.visited the self.dfs that pkg
        # return the self.order reversed [::-1]


    def _dfs(self, pkg):
        if pkg in self.visiting:
            raise ValueError(f"Cyclic dependency detected involving '{pkg}'")

        if pkg in self.visited:
            return

        self.visiting.add(pkg)

        for dep in self.deps.get(pkg, []):
            self._dfs(dep)

        self.visiting.remove(pkg)   # no longer exploring this - remove an item from the set
        self.visited.add(pkg)       # this is now finished - add an item to the set
        self.order.append(pkg)      # add pkg to the end of the list
    # check if is already being visiting - if so raise valueerror
    # check if is already visted - if so return
    # add in self.visiting
    # iterate for other deps of the pkg and for each one run self dfs
    # remove from visiting
    # add in visited
    # append in order list


def resolve_dependencies(deps: dict[str, list[str]]) -> list[str]:
    return DependencyResolver(deps).resolve()
# execute the class and call the resolve func on it


print(resolve_dependencies({'app': ['lib1', 'lib2'], 'lib1': ['core'], 'lib2': ['core'], 'core': []}))  # ['app', 'lib2', 'lib1', 'core']
print(resolve_dependencies({'a': ['b'], 'b': ['c'], 'c': []}))                                          # ['a', 'b', 'c']
print(resolve_dependencies({'a': []}))                                                                  # ['a']


# SETUP (when object is created):
#     deps     = the dependency dictionary
#     visited  = empty set   (packages fully done)
#     visiting = empty set   (packages being explored right now — for cycle detection)
#     order    = empty list  (result, built up as packages finish)

# resolve():                          # the driver
#     for each package in deps:
#         if package not already visited:
#             dfs(package)
#     return order reversed

# dfs(package):                       # the recursive worker
#     if package is in visiting:      # reached one we're still exploring
#         raise error (cycle!)        # -> impossible loop
#     if package is already visited:
#         return                      # nothing to do

#     mark package as visiting

#     for each dependency of package:
#         dfs(dependency)             # finish dependencies FIRST (recursion)

#     unmark package from visiting
#     mark package as visited
#     add package to order            # recorded AFTER its dependencies



# deps = {
#     'app':  ['lib1', 'lib2'],   # 'app' depends on lib1 and lib2
#     'lib1': ['core'],           # 'lib1' depends on core
#     'lib2': ['core'],           # 'lib2' depends on core
#     'core': []                  # 'core' depends on nothing
# }
# pkg = 'app'     # then later 'lib1', 'lib2', 'core', ...