# ex4-2 - resolve_dependencies
# attempt: try1.py
# (signature pre-filled from the .en; write your solution below)

class DependecyResove:
    def __init__(self,deps):
        self.deps=deps # SELF DEPS FROM PARAMS
        self.visiting=set() # AN EMPTY SET FOR VISITNG - DEPS ALREADY CHECKING
        self.visited=set() # AN EMPTY SET FOR VISITED - WHAT ALREADY DONE
        self.order=[] # AN EMPTY LIST FOR THE COMPLETED ORDER OF DEPENDECIES

    # WE CREATEA A FUNCTION WICH WE CALL IT IN MAIN FUNCTION
    def resolve(self):
        for pkg in self.deps: # iterate over all deps
            if pkg not in self.visited: # if not in visited set
                self._dfs(pkg) # then run dfs on it

        return self.order[::-1] # return the reverse order of depemdecies list

    def _dfs(self,pkg):
        if pkg in self.visiting: # check if in visting 
            raise ValueError("it is already visiting") # if so raise a value error
        
        if pkg in self.visited: # check if in visited 
            return # if so return

        # add in visiting list
        self.visiting.add(pkg)
        
        for dep in self.deps.get(pkg,[]): # recursive all dependencies of the pkg
            self._dfs(dep) # and run self dfs on them
    
        self.visiting.remove(pkg) # remove from visiting
        self.visited.add(pkg) # add in visited
        self.order.append(pkg) # add on order
        
def resolve_dependencies(deps: dict[str, list[str]]) -> list[str]:
    return DependecyResove(deps).resolve()


print(resolve_dependencies({'app': ['lib1', 'lib2'], 'lib1': ['core'], 'lib2': ['core'], 'core': []}))  # ['app', 'lib2', 'lib1', 'core']
print(resolve_dependencies({'a': ['b'], 'b': ['c'], 'c': []}))                                          # ['a', 'b', 'c']
print(resolve_dependencies({'a': []}))
