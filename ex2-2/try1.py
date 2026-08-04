# ex2-2 - sliding_w_m
# attempt: try1.py
# (signature pre-filled from the .en; write your solution below)

def sliding_w_m(nums: list[int], k: int) -> list[int]:
    if not nums or len(nums) <= k <= 0: # check if nums is empty or bigger then nums or is 0
        return []

    result = [] # decalre a list of max
    for i in range(len(nums)-k + 1): # iterate over len of nums - k
        window = nums[i:i+k] # find windows of each iteration
        result.append(max(window)) # find maximum of each window and append in results

    return result

print(sliding_w_m([1, 2, 3, 1, 4, 5, 2, 3, 6], 3)) #     [3, 3, 4, 5, 5, 5, 6]
print(sliding_w_m([1, 2, 3], 2)) #   [2, 3]
print(sliding_w_m([1, 3, 2, 5, 4], 1)) #     [1, 3, 2, 5, 4]
print(sliding_w_m([1], 3)) #     []
print(sliding_w_m([1, 2], 8)) #  []
print(sliding_w_m([], 3)) #  []