# ex3-2 - arr_rotation_detector
# attempt: try1.py
# (signature pre-filled from the .en; write your solution below)

def arr_rotation_detector(arr1: list[int], arr2: list[int]) -> bool:
    # 1. if different lengths return false
    if len(arr1) != len(arr2):
        return False

    # 2. if both empty return true
    if not arr1 and not arr2:
        return True

    # 3. iterate over len arr1 and reorder and compare with arr2
    for i in range(len(arr1)):
        reordered = arr1[i:]+arr1[:i]
        if reordered == arr2:
            return True

    return False

