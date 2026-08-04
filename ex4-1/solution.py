from collections import deque


def shortest_path(grid: list[list[int]]) -> int:
    if not grid:
        return -1

    rows, cols = len(grid), len(grid[0])
    if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
        return -1

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(0, 0, 0)])      # row, col, distance in moves
    visited = {(0, 0)}

    while queue:
        row, col, distance = queue.popleft()
        if row == rows - 1 and col == cols - 1:
            return distance

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if not (0 <= new_row < rows and 0 <= new_col < cols):
                continue
            if grid[new_row][new_col] == 1:
                continue
            if (new_row, new_col) in visited:
                continue
            visited.add((new_row, new_col))
            queue.append((new_row, new_col, distance + 1))

    return -1
