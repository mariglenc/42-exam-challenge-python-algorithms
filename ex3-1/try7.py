# ex3-1 - constellation_mapper
# attempt: try7.py
# (signature pre-filled from the .en; write your solution below)

def constellation_mapper(stars: list[tuple[int, int]], size: int) -> list[str]:
    grid_outer = []
    for _ in range(size):
        inner_list = []
        for _ in range(size):
            inner_list.append('.')
        grid_outer.append(inner_list)

    for (row, col) in stars:
        if 0 <= row <= size and 0<=col<=size:
            grid_outer[row][col]="*"

    grid_final = []
    for lst in grid_outer:
        grid_final.append("".join(lst))

    return grid_final

