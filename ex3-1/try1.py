# ex3-1 - constellation_mapper
# attempt: try1.py
# (signature pre-filled from the .en; write your solution below)

def constellation_mapper(stars: list[tuple[int, int]], size: int) -> list[str]:
    # 1. create an empty grid: a list of rows, each row a list of '.'
    grid_list = []
    for _ in range(size): # first iteration is to add the list of dots into grid list
        inner_list = [] # declare inner list
        for _ in range(size): # iterate again over range of size
            inner_list.append('.') # append '.' into inner list

        grid_list.append(inner_list) # each inner list append into grid_list

    # 2. Place the stars
    for (row, column) in stars:                       # each star is a (row, col) tuple
        if 0 <= row < size and 0 <= column < size:    # the list of touples (row,col) should be less than size
            grid_list[row][column] = '*' # add a star *

    # 3. Turn each row (a list of chars) into a single string
    result = []
    for row in grid_list:
        inner_list_to_string = "".join(row)   # join the list elements with empty string ['.', '*', '.'] -> ".*."
        result.append(inner_list_to_string)

    return result

# create the grid 
    # iterate first time to create the gird list outer one
    # iterate over each inner list and append only '.'
    # on the inner iteration compelete append the inner list to the grid outer list

# place stars
    # iterate over star list
    # valideate row and column of lists if they are bigger equeal to 0 and less the size
    # if so append a star in that gridlist[row][column]

# turn each inner list row into a string
    # iterate over gird list
    # each inner list join with empty string
    # that string append to the result
    
    # return result


# [
#   ['.', '.', '.'], 
#   ['.', '.', '.'], 
#   ['.', '.', '.']
# ]

print(constellation_mapper([(4,4), (5, 1), (2, 2)], 3)) # ['*..', '.*.', '..*']

