# ex2-1 - list_intersection
# attempt: try3.py
# (signature pre-filled from the .en; write your solution below)

def list_intersection(lists: list[list[int]]) -> list[int]:
    if not lists:
        return []

    common = set(lists[0])

    for lst in lists[1:]:
        common = common & set(lst)

    return sorted(common)

