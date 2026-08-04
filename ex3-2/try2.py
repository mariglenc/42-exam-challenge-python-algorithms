# ex3-2 - arr_rotation_detector
# attempt: try2.py
# (signature pre-filled from the .en; write your solution below)

def arr_rotation_detector(arr1: list[int], arr2: list[int]) -> bool:
    # if lenght not same return false 
    if len(arr1) != len(arr2):
        return False
    
    # if both empty return true 
    if not arr1 and not arr2:
        return True
    
    # iterate over arr 1 len 
    # reorder arr 1
    # if arr 1 equal arr2 return True
    # after iteration return False
    for i in range(len(arr1)):
        reorder = arr1[i:] + arr1[:i]
        # if the reoredered arr1 is eq with arr2 return true
        if reorder == arr2:
            return True

    return False

