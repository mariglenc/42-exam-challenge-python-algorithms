# ex3-2 - arr_rotation_detector
# attempt: try6.py
# (signature pre-filled from the .en; write your solution below)

def arr_rotation_detector(arr1: list[int], arr2: list[int]) -> bool:
    if len(arr1) != len(arr2):
        return False

    if not arr1 and not arr2:
        return True

    for i in range(len(arr1)):
        reversed_arr1 = arr1[-i:]+arr1[:-i]
        if reversed_arr1 == arr2:
            return True

    return False
