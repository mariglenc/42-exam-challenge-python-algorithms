# ex1-2 - merge_sort_unique
# attempt: try4.py
# (signature pre-filled from the .en; write your solution below)

def merge_sort_unique(lists: list[list[int]]) -> list[int]:
    merged_list = []
    for inner_ls in lists:
        for item in inner_ls:
            merged_list.append(item)
    unique = set(merged_list)

    return sorted(unique)

