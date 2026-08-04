# ex3-1 - constellation_mapper
# attempt: try2.py
# (signature pre-filled from the .en; write your solution below)

def constellation_mapper(stars: list[tuple[int, int]], size: int) -> list[str]:

    # 1.create the grid with '.'
    grid_list = []
    for _ in range(size):
        inner_list = []
        for _ in range(size):
            inner_list.append('.')
        grid_list.append(inner_list)


    # 2.place the stars in their place
    for (row, column) in stars:
        if 0 <= row < size and 0 <= column < size:
            grid_list[row][column]="*"

    # 3.convert each inner list into a string with "".join(inner_list) 
    result = []
    for inner_list in grid_list:
        inner_list_to_String = "".join(inner_list)
        result.append(inner_list_to_String)

    return result
