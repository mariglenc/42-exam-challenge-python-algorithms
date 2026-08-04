
def list_intersection(lists: list[list[int]]) -> list[int]:
    if not lists:              # if the outer list is empty
        return lists           # return [] (lists is already the empty list)

    common = set(lists[0])     # We start with the first list so the loop has something to intersect against

    for lst in lists[1:]:      # go through the REST of the inner lists (skip the first)
        common &= set(lst)     # keep only numbers that are in BOTH common AND this list

    return sorted(common)      # sort the survivors ascending, return as a list
