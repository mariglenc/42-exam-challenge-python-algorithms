# def constellation_mapper(stars: list[tuple[int, int]], size: int) -> list[str]:
#     s = set(stars)
#     return ["".join('*' if (r, c) in s else '.' for c in range(size)) for r in range(size)]

def constellation_mapper(stars: list[tuple[int, int]], size: int) -> list[str]:
    # 1. Build an empty grid: a list of rows, each row a list of '.'
    grid = []
    for r in range(size):          # for each row 0..size-1
        row = []
        for c in range(size):      # for each column 0..size-1
            row.append('.')        # start every cell as a dot
        grid.append(row)

    # 2. Place the stars
    for (r, c) in stars:                       # each star is a (row, col) tuple
        if 0 <= r < size and 0 <= c < size:    # only if it's inside the grid
            grid[r][c] = '*'                    # mark that cell with a star

    # 3. Turn each row (a list of chars) into a single string
    result = []
    for row in grid:
        result.append("".join(row))   # ['.', '*', '.'] -> ".*."
    return result

# print(constellation_mapper([(0, 0), (1, 1), (2, 2)], 3)) # ['*..', '.*.', '..*']
# print(constellation_mapper([(1, 1), (0, 1), (2, 1), (1, 0), (1, 2)], 3)) # ['.*.', '***', '.*.']
# print(constellation_mapper([], 2)) # ['..', '..']
# print(constellation_mapper([(0, 0), (5, 5)], 3)) # ['*..', '...', '...']
# print(constellation_mapper([(0, 1), (1, 1), (2, 1)], 3)) # ['.*.', '.*.', '.*.']
