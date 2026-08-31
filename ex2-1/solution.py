def spiral_waver(size: int) -> list[list[int]]:
    if size <= 0:
        return []

    # list repetition
    matrix = []
    for _ in range(size):
        matrix.append([0] * size)

    # drawing the starting fence around the grid.
    top_row = 0
    bottom_row = size - 1
    left_col = 0
    right_col = size - 1

    num = 1     # holds the next number to be written into the grid
    while num <= size * size:

        # left -> right, along the top
        for col in range(left_col, right_col + 1):          # iterate over the rows from left col to right col
            matrix[top_row][col] = num                      # fill each col of the the first row 
            num += 1                                        # increase num for each filled col
        top_row += 1                                        # increase top row with 1

        # top -> bottom, along the right
        for row in range(top_row, bottom_row + 1):          # iterate over rows from top to bottom
            matrix[row][right_col] = num                    # fill each last col of all rows
            num += 1                                        # increase the num for each filled last col row
        right_col -= 1                                      # sinve the outer left col is filled decrease by 1

        # right -> left, along the bottom
        if top_row <= bottom_row:                           # skip if only one row was left — it's already filled
            for col in range(right_col, left_col - 1, -1):  # iterate on the rverse remaining cols
                matrix[bottom_row][col] = num               # fill each col on reverse
                num += 1                                    # incerase num for each filled reverse col of last row with 1
            bottom_row -= 1                                 # since bottom row is completed decrease with 1

        # bottom -> top, along the left
        if left_col <= right_col:                           # skip if only one column was left — it's already filled
            for row in range(bottom_row, top_row - 1, -1):  # iterate over each row in reverse from bottom to the top
                matrix[row][left_col] = num                 # fill each left col on the reverse
                num += 1                                    # as always increase the num with one
            left_col += 1                                   # since left col was filled increase with one

    return matrix
