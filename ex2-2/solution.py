# def sliding_w_m(nums: list[int], k: int) -> list[int]:
#     if not nums or k <= 0 or k > len(nums):
#         return []

#     return [max(nums[i:i+k]) for i in range(len(nums) - k + 1)]

def sliding_w_m(nums: list[int], k: int) -> list[int]:
    # guard: empty list, bad k, or window bigger than the list
    if not nums or k <= 0 or k > len(nums):
        return []

    result = []
    for i in range(len(nums) - k + 1):      # each starting position of the window
        window = nums[i:i+k]                # grab k items starting at i
        result.append(max(window))          # store the biggest in that window
    return result

# print(sliding_w_m([1, 2, 3, 1, 4, 5, 2, 3, 6], 3)) # [3, 3, 4, 5, 5, 5, 6]))
# print(sliding_w_m([1, 2, 3], 2)) # [2, 3]))
# print(sliding_w_m([1, 3, 2, 5, 4], 1)) # [1, 3, 2, 5, 4]))
# print(sliding_w_m([1], 3)) # []))
# print(sliding_w_m([1, 2], 8)) # []))
# print(sliding_w_m([], 3)) # []))