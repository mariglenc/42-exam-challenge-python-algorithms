def island_matrix_counter(matrix: list[list[str]]) -> int:
    if not matrix:
        return 0

    islands = 0

    def dfs(r, c):
        if (
            r < 0 or c < 0 or
            r >= len(matrix) or
            c >= len(matrix[0]) or
            matrix[r][c] == "0"     # water
        ):
            return

        matrix[r][c] = "0"          # sink the cell so it is not counted twice

        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == "1":
                islands += 1
                dfs(r, c)

    return islands


if __name__ == "__main__":
    print(island_matrix_counter([
        ["1", "1", "1", "1", "0"],
        ["1", "1", "1", "0", "0"],
        ["1", "1", "1", "1", "0"],
        ["0", "0", "0", "0", "0"],
    ]))  # 1
    print(island_matrix_counter([
        ["0", "0", "0", "1"],
        ["1", "0", "0", "1"],
        ["0", "0", "1", "0"],
    ]))  # 3
