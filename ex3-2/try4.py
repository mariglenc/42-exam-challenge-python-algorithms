# ex3-2 - arr_rotation_detector
# attempt: try4.py
# (signature pre-filled from the .en; write your solution below)

def arr_rotation_detector(arr1: list[int], arr2: list[int]) -> bool:
    if len(arr1) != len(arr2): # if the lengths are different
        return False # return false

    if not arr1 and not arr2: # if both lists arr1 and arr2 are empty
        return True # return true

    for i in range(len(arr1)): # iterate over length of arr1
        revesed_arr1 = arr1[-i:]+arr1[:-i] # reverse arr1 on index -> arr1[-i:] + arr1[:-i]
        if revesed_arr1 == arr2: # if reversed one is eq to arr2
            return True # return true
    
    return False # else return false
