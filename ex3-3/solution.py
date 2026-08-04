def spiral_waver(size: int) -> list[list[int]]:
    if size <= 0:
        return []

    matrix = [[0] * size for _ in range(size)]

    top, bottom = 0, size - 1
    left, right = 0, size - 1
    num = 1

    while num <= size * size:
        # left -> right along the top row
        for col in range(left, right + 1):
            matrix[top][col] = num
            num += 1
        top += 1

        # top -> bottom along the right column
        for row in range(top, bottom + 1):
            matrix[row][right] = num
            num += 1
        right -= 1

        # right -> left along the bottom row
        if top <= bottom:
            for col in range(right, left - 1, -1):
                matrix[bottom][col] = num
                num += 1
            bottom -= 1

        # bottom -> top along the left column
        if left <= right:
            for row in range(bottom, top - 1, -1):
                matrix[row][left] = num
                num += 1
            left += 1

    return matrix


if __name__ == "__main__":
    print(spiral_waver(1))   # [[1]]
    print(spiral_waver(3))   # [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
    print(spiral_waver(4))   # [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
