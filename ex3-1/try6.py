# ex3-1 - constellation_mapper
# attempt: try6.py
# (signature pre-filled from the .en; write your solution below)

def constellation_mapper(stars: list[tuple[int, int]], size: int) -> list[str]:
    #1- create the grid outer
    grid_outer = []
    for _ in range(size):
        inner_list = []
        for _ in range(size):
            inner_list.append(".")
        grid_outer.append(inner_list)

    #2-validate row col and add stars
    for (row,col) in stars:
        if 0 <= row <= size and 0 <= col <= size:
            grid_outer[row][col] = "*"

    #3 convert inner list to strng with "".join
    final_value=[]
    for lst in grid_outer:
        final_value.append("".join(lst))

    return final_value
