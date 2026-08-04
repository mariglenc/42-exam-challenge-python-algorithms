# ex2-2 - sliding_w_m
# attempt: try2.py
# (signature pre-filled from the .en; write your solution below)

def sliding_w_m(nums: list[int], k: int) -> list[int]:
    if not nums or len(nums) <= k <= 0: # if not nums or k bigger than length or 0
        return []

    result = []
    for i in range(len(nums)-k + 1):
        window = nums[i:i+k]
        result.append(max(window))

    return result
