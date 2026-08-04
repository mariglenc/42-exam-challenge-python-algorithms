# def spiral_waver(size: int) -> list[list[int]]:
#     if not size or size <= 0:
#         return []

#     matrix = [[0] * size for _ in range(size)]

#     top = 0
#     bottom = size - 1
#     left = 0
#     right = size - 1

#     num = 1

#     while left <= right and top <= bottom:
#         for col in range(left, right + 1):
#             matrix[top][col] = num
#             num += 1

#         top += 1
#         for row in range(top, bottom + 1):
#             matrix[row][right] = num
#             num += 1

#         right -= 1
#         for col in range(right, left - 1, -1):
#             matrix[bottom][col] = num
#             num += 1

#         bottom -= 1

#         for row in range(bottom, top - 1, -1):
#             matrix[row][left] = num
#             num += 1

#         left += 1

#     return matrix

def spiral_waver(size: int) -> list[list[int]]:
    if not size or size <= 0:
        return []

    matrix = [[0] * size for _ in range(size)]

    top = 0
    bottom = size - 1
    left = 0
    right = size - 1

    num = 1
    while left <= right and top <= bottom:
        for col in range(left, right + 1):
            matrix[top][col] = num
            num += 1

        top += 1
        for row in range(top, bottom + 1):
            matrix[row][right] = num
            num += 1

        right -= 1
        for col in range(right, left - 1, -1):
            matrix[bottom][col] = num
            num += 1

        bottom -= 1
        for row in range(bottom, top -1, -1):
            matrix[row][left] = num
            num += 1

        left += 1


    return matrix




print(spiral_waver(-1))  # []
print(spiral_waver(0))   # []
print(spiral_waver(1))   # [[1]]        
print(spiral_waver(2))   # [[1, 2], [4, 3]]
print(spiral_waver(3))   # [[1, 2, 3], [8, 9, 4], [7, 6, 5]
print(spiral_waver(4))