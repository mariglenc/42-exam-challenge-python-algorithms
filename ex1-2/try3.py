# ex1-2 - merge_sort_unique
# attempt: try3.py
# (signature pre-filled from the .en; write your solution below)

def merge_sort_unique(lists: list[list[int]]) -> list[int]:
    merged_inner = [] # declare a merged inner list
    for lis in lists: # iterate over big lists
        for item in lis: # iterate on inners lis items
            merged_inner.append(item) # append each item to the merged inner
        
    unique = set(merged_inner) # make them unique with set
    
    return sorted(unique) # then sort them and return a list with sorted
