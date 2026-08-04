# ex3-1 - constellation_mapper
# attempt: try4.py
# (signature pre-filled from the .en; write your solution below)

def constellation_mapper(stars: list[tuple[int, int]], size: int) -> list[str]:
    # create the grid_list = [] with only dots
    grid_list = []
    for _ in range(size):
        inner_list = []
        for _ in range(size):
            inner_list.append(".")
        grid_list.append(inner_list)

    # put the stars then in it
    for (row, col) in stars:
        if 0 <= row <= size and 0 <= col <= size:
            grid_list[row][col] = "*"

    result = []
    for inner_list in grid_list:
        result.append("".join(inner_list))

    return result

