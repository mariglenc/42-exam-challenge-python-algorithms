# def merge_sort_unique(lists: list[list[int]]) -> list[int]:
#     return sorted(set(x for y in lists for x in y))
# x        for y in lists    for x in y
# ↑            ↑                 ↑
# collect   outer loop        inner loop
# this      (each list)      (each number)

def merge_sort_unique(lists: list[list[int]]) -> list[int]:
    merged = []
    for inner in lists:          # go through each inner list
        for num in inner:        # go through each number in it
            merged.append(num)   # collect all numbers into one flat list
    unique = set(merged)         # set() removes duplicates
    return sorted(unique)        # sort ascending, return as a list
