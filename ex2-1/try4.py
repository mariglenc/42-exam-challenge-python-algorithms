# ex2-1 - list_intersection
# attempt: try4.py
# (signature pre-filled from the .en; write your solution below)

def list_intersection(lists: list[list[int]]) -> list[int]:
    if not lists:
        return []

    common_nr = set(lists[0])
    for lis in lists[1:]:
        common_nr = common_nr & set(lis)

    return sorted(common_nr)
