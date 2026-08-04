def island_matrix_counter(matrix: list[list[int]]) -> int:
    if not matrix:
        return 0

    island = 0

    def dfs(r, c):
        if (r < 0 or c < 0 or    
        r >= len(matrix) or c >= len(matrix[0]) or
        matrix[0][0] == '0'):

            return

        matrix[r][c] == '0'

        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == '1':
                island += 1
                dfs(r, c)

    return island

print(island_matrix_counter([
    ['0', '0', '0', '1'],
    ['1', '0', '0', '1'],
    ['0', '0', '1', '0']
]))