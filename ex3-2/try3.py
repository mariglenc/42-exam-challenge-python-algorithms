# ex3-2 - arr_rotation_detector
# attempt: try3.py
# (signature pre-filled from the .en; write your solution below)

def arr_rotation_detector(arr1: list[int], arr2: list[int]) -> bool:
    # if the lengths are different it is a false
    if len(arr1) != len(arr2):
        return False
    
    # if both empty return true
    if not arr1 and not arr2:
        return True
    
    # reorder only arr1 and on each iteration/reorder compare it to arr2
    
    for i in range(len(arr1)):
        reorder_arr1 = arr1[i:] + arr1[:i]
        if reorder_arr1 == arr2:
            return True
    return False
