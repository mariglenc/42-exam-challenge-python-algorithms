def spiral_waver(size):
    if size <= 0:
        return []

    matrix = [[0] * size for _ in range(size)]

    # drejtimet: djathtas, poshtë, majtas, lart
    directions = [
        (0, 1),
        (1, 0),
        (0, -1),
        (-1, 0)
    ]

    row = 0
    col = 0
    direction = 0

    for num in range(1, size * size + 1):
        matrix[row][col] = num

        # pozicioni i ardhshëm
        new_row = row + directions[direction][0]
        new_col = col + directions[direction][1]

        # nëse dalim jashtë ose qeliza është mbushur
        if (
            new_row < 0 or new_row >= size or
            new_col < 0 or new_col >= size or
            matrix[new_row][new_col] != 0
        ):
            direction = (direction + 1) % 4

            new_row = row + directions[direction][0]
            new_col = col + directions[direction][1]

        row = new_row
        col = new_col

    return matrix



print(spiral_waver(-1))  # []
print(spiral_waver(0))   # []
print(spiral_waver(1))   # [[1]]
print(spiral_waver(2))   # [[1, 2], [4, 3]]
print(spiral_waver(3))   # [[1, 2, 3], [8, 9, 4], [7, 6, 5]]