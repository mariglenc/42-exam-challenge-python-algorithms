# ex1-2 - merge_sort_unique
# attempt: try2.py
# (signature pre-filled from the .en; write your solution below)

def merge_sort_unique(lists: list[list[int]]) -> list[int]:
    merged = []
    for list in lists:
        for item in list:
            merged.append(item)
    unique = set(merged)
    return sorted(unique)



print(merge_sort_unique([[1, 3, 5], [2, 3, 6], [1, 7]])) # -> [1, 2, 3, 5, 6, 7]

