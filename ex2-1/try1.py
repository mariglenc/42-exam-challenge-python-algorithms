# ex2-1 - spiral_waver
# attempt: try1.py
# (signature pre-filled from the .en; write your solution below)

def spiral_waver(size: int) -> list[list[int]]:

    if size <= 0:
        return []

    matrix = []
    for _ in range(size):
        matrix.append([0]*size)

    top_row = 0
    bottom_row = size - 1
    left_col = 0
    right_col = size - 1

    num = 1

    while num <= size*size:
        for col in range(left_col, right_col + 1):
            matrix[top_row][col] = num
            num += 1
        top_row += 1

        for row in range(top_row, bottom_row + 1):
            matrix[row][right_col] = num
            num += 1
        right_col -= 1

        if top_row <= bottom_row:
            for col in range(right_col, left_col - 1, -1):
                matrix[bottom_row][col] = num
                num += 1
            bottom_row -= 1

        if left_col <= right_col:
            for row in range(bottom_row, top_row - 1, -1):
                matrix[row][left_col] = num
                num += 1
            left_col += 1

    return matrix
