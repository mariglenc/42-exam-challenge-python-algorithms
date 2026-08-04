# ex1-2 - merge_sort_unique
# attempt: try1.py
# (signature pre-filled from the .en; write your solution below)

def merge_sort_unique(lists: list[list[int]]) -> list[int]:
    merged_inner = []
    for list in lists:
        for items in list:
            merged_inner.append(items)
    unique = set(merged_inner)

    return sorted(unique)
