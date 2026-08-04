# ex2-1 - list_intersection
# attempt: try5.py
# (signature pre-filled from the .en; write your solution below)

def list_intersection(lists: list[list[int]]) -> list[int]:
    if not lists:
        return []
    
    commons_int = set(lists[0])
    for ls in lists[1:]:
        commons_int = commons_int & set(ls)

    return sorted(commons_int)

# print(list_intersection([[5, 4, 3], [2, 1, 3], [2, 1, 3]]) )#-> [3]