# ex2-2 - sliding_w_m
# attempt: try5.py
# (signature pre-filled from the .en; write your solution below)

def sliding_w_m(nums: list[int], k: int) -> list[int]:
    if not nums or len(nums) < k:
        return []
    
    max_slided_nr = []
    for i in range(len(nums) - k + 1):
        window = nums[i:i+k]
        max_slided_nr.append(max(window))

    return max_slided_nr
