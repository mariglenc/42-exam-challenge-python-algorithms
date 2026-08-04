# ex2-2 - sliding_w_m
# attempt: try4.py
# (signature pre-filled from the .en; write your solution below)

def sliding_w_m(nums: list[int], k: int) -> list[int]:
    if not nums or len(nums) < k:  # check if nums empty or  lower than k if so return []
        return []

    max_slided = [] # declare max slided list
    for i in range(len(nums)-k + 1): # iterate over range of len nums - k + 1
        window = nums[i:i+k] # create the windows list with index i and i+k
        max_slided.append(max(window)) # find the max nr of each window
    
    return max_slided # return the max slided window

