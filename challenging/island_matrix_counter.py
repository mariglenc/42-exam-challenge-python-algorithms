# def island_matrix_counter(matrix: list[list[str]]) -> int:
#     if not matrix or not matrix[0]:
#         return 0

#     rows, cols = len(matrix), len(matrix[0])
#     islands = 0

#     def dfs(r, c):
#         if r < 0 or r >= rows or c < 0 or c >= cols or matrix[r][c] != "1":
#             return

#         matrix[r][c] = "0"

#         dfs(r + 1, c)
#         dfs(r - 1, c)
#         dfs(r, c + 1)
#         dfs(r, c - 1)

#     for r in range(rows):
#         for c in range(cols):
#             if matrix[r][c] == "1":
#                 islands += 1
#                 dfs(r, c)

#     return islands


# print(island_matrix_counter([
#     ["1", "1", "1", "1", "0"],
#     ["1", "1", "1", "0", "0"],
#     ["1", "1", "1", "1", "0"],
#     ["0", "0", "0", "0", "0"]
# ]))

# print(island_matrix_counter([
#     ["1", "1", "1", "1", "0"],
#     ["1", "1", "1", "0", "0"],
#     ["0", "1", "0", "1", "0"],
#     ["0", "0", "0", "0", "0"]
# ]))


def island_matrix_counter(matrix):
    if not matrix:
        return 0

    islands = 0

    def dfs(r, c):
        if (
            r < 0 or c < 0 or
            r >= len(matrix) or
            c >= len(matrix[0]) or
            matrix[r][c] == "0"  #uje
        ):
            return

        matrix[r][c] = "0"

        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == "1":
                islands += 1
                dfs(r, c)

    return islands

print(island_matrix_counter([
    ["1", "1", "1", "1", "0"],
    ["1", "1", "1", "0", "0"],
    ["1", "1", "1", "1", "0"],
    ["0", "0", "0", "0", "0"]
]))
print(island_matrix_counter([
    [0, 0, 0, 1],
    [1, 0, 0, 1],
    [0, 0, 1, 0]
]))

# print(island_matrix_counter([
#     ["1", "1", "1", "1", "0"],
#     ["1", "1", "1", "0", "0"],
#     ["0", "1", "0", "1", "0"],
#     ["0", "0", "0", "0", "0"]
# ]))
