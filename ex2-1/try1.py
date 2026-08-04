# ex2-1 - list_intersection
# attempt: try1.py
# (signature pre-filled from the .en; write your solution below)

def list_intersection(lists: list[list[int]]) -> list[int]:
    if not lists:
        return [] # if lists is empty return empty list
    
    commons = set(lists[0]) # start the first set of the first inner list

    for list in lists[1:]: # iterate over the big list 
        commons = commons & set(list) # and here the first common set intersetcs with

    return sorted(commons)
