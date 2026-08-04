from collections import deque


def shortest_path(grid: list[list[int]]) -> int:
    if not grid:
        return -1

    if grid[0][0] == 1:
        return -1
    dirs = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]
    rows = len(grid)
    cols = len(grid[0])

    if grid[rows - 1][cols - 1] == 1:
        return -1
    visited = {(0, 0)}
    queue = deque([(0, 0)])
    while queue:
        r, c = queue.popleft()
        if r == rows - 1 and c == cols - 1:
            return moves
        for dr, dc in dirs:
            new_row = r + dr
            new_col = c + dc

            if not (0 <= new_row < rows and 0 <= new_col < cols):
                continue
            if grid[new_row][new_col] == 1:
                continue
            if (new_row, new_col) in visited:
                continue

            visited.add((new_row, new_col))
            queue.append((new_row, new_col))
        moves += 1

    return -1

# from collections import deque

# def shortest_path(grid: list[list[int]]) -> int:
#     if not grid:
#         return -1

#     rows = len(grid)
#     cols = len(grid[0])

#     if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
#         return -1

#     directions = [
#         (-1, 0),   # up
#         (1, 0),    # down
#         (0, -1),   # left
#         (0, 1)     # right
#     ]

#     queue = deque([(0, 0, 0)])   # row, col, distance
#     visited = {(0, 0)}

#     while queue:
#         row, col, distance = queue.popleft()

#         if row == rows - 1 and col == cols - 1:
#             return distance

#         for dr, dc in directions:
#             new_row = row + dr
#             new_col = col + dc

#             if not (0 <= new_row < rows and 0 <= new_col < cols):
#                 continue

#             if grid[new_row][new_col] == 1:
#                 continue

#             if (new_row, new_col) in visited:
#                 continue

#             visited.add((new_row, new_col))
#             queue.append((new_row, new_col, distance + 1))

#     return -1


print(shortest_path([
    [0,0,0],
    [1,1,0],
    [0,0,0],
    [0,0,0],
    [1,0,0]
]))