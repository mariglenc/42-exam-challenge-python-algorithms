# def arr_rotation_detector(arr1: list[int], arr2: list[int]) -> bool:
#     if len(arr1) != len(arr2):
#         return False

#     if not arr1 and not arr2:
#         return True

#     return any(
#         arr2 == arr1[i:] + arr1[:i]
#         for i in range(len(arr1))
#     )

def arr_rotation_detector(arr1: list[int], arr2: list[int]) -> bool:
    # 1.different lengths -> never a rotation
    if len(arr1) != len(arr2):
        return False

    # 2.both empty -> counts as a rotation
    if not arr1 and not arr2:
        return True

    # 3. iterate over len arr1 and reorder and compare
    for i in range(len(arr1)):          # try every possible starting offset
        rotated = arr1[i:] + arr1[:i]   # rotate arr1 so it starts at index i
        if rotated == arr2:             # does this rotation match arr2?
            return True                 # yes -> it's a rotation

    return False                        # no offset matched -> not a rotation


# 1 check lengths if different return false
# 2 check if both empty return true
# iterate over arr1
    # on each iterateion roteate arr retgarding the index
    # on each iterateion compare the new rotated arr1 with arr2
    # if equal return true
    # then return false
