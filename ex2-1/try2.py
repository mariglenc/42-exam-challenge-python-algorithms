# ex2-1 - list_intersection
# attempt: try2.py
# (signature pre-filled from the .en; write your solution below)

def list_intersection(lists: list[list[int]]) -> list[int]:
    if not lists:
        return []

    commons = set(lists[0])

    for list in lists[1:]:
        commons = commons & set(list)
    
    return sorted(commons)
