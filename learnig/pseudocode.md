ex1-1
    declare a sorted_list list
    iterate over all list items of lst
    on each iteration append the sorted items to the seorted list 
    return sorted list

ex1-2
    declare a merged list
    iterate over all list of lists 
        inside that iterate over all items of the list
        appen items into merged
    get unqiue with set -> which brings a dictionary
    return the sorted of unique which brings back a list

ex2-1
    if  lists is empty return empty list []
    create a new set of commons with the first item of the list
    iterate over the lists[1:] (because the first item iused )
        on each iteration find an intesection of common with the set list of iterated item
    
    at the inde return a sorted commons

ex2-2
    if not list or len list is lower than k return []
    declare a max_slided list
    now iterate over range of len list - k + 1
        declare window with index i : i+k
        append to the max_slided of each window
    
    return max_slided

ex3-1
    1-create the grid    
        declare gird outer
        iterate over range len of size
            declare inner_list
            iterate again over range len of size
                insert '.' in inner_list
            append inner_list in grid outer
    
    2-insert * in the grid
        iterate over rows cols of the starrs
            if the row is eq bigger than 0 and les eq than size
                insert to grid row col = "*"
    
    3-convert the inner list to a string
        declare a result list
        iterate over grid outer
            on each item of it "".join
            and append to result
        return result

ex3-2
    if len not same return false and if both empty return true
    iterate over len of arr1
        reverse arr1 and on each iteration compare to arr2
            if the same return true
    at the end of iteration return false

ex4-1
    def is palindorme
        shrink the text with start end params
        check if it is eq with its reversed one
    
    def min cuts 
        if start >= end or is palidnrome then return 0
        def the feust cuts nr to float inf
        iterate over the start end
            cut = 1 + split: from start to split  and from split + 1 to end -> 1 + because one split
  
        EXAMPLE ------------------ min_cuts
        min_cuts('aab')          ← "aab" isn't a palindrome, so try every cut:

        try cut: 'a' | 'ab'    ← cut after 1st letter
            'a'  → 0 cuts (palindrome)
            'ab' → not a palindrome, so IT tries cuts too:
                'a' | 'b' → 0 + 0, plus 1 cut = 1
            so this option = 1 (this cut) + 0 + 1 = 2

        try cut: 'aa' | 'b'    ← cut after 2nd letter
            'aa' → 0 cuts (palindrome!)
            'b'  → 0 cuts
            so this option = 1 (this cut) + 0 + 0 = 1  ← better!

        BEST = min(2, 1) = 1
        EXAMPLE ------------------
        
ex4-2
    declare the class DependencyResolve:
        constructor:
            self.deps=deps
            self.validating=set()
            self.validated=set()
            self.order=[]

    declade resolve self 
        iterate pkg of deps
        if pkg is not in visted 
            self dfs on it
        return orders
    declare dfs (slef, pkg)
        if pkg in visiting
            raise valuerror
        if dfs in visted
            return
        
        self.visiting.add pkg

        iterate over dep of pg
            if so self dfs again
        
        self visiting remove
        self visited add
        self order appen

    call the classs(deps).resolve()
    
