# Expected files : prism_detector.py
# Allowed functions: None
# Write a function that finds all occurrences of a pattern in a 2D grid.
# Your function must be declared as follows:
# def prism_detector(grid: list[str], pattern: str) -> list [tuple[int, int, str]]:

# The function should:
# Take a 2D grid (list of strings) and a pattern string to search for Search in all 8 directions: horizontal, vertical, and diagonal (both ways)
# Return a list of tuples with starting positions and direction codes Handle empty grids and empty patterns correctly
# Return empty list if no matches found

# Search directions:
# Horizontal (left to right and right to left)
# Vertical (top to bottom and bottom to top)
# Diagonal (both diagonals, both directions)

# Direction codes:
# "H" Horizontal (left to right)
# Horizontal (right to left) "H-
# "V" Vertical (top to bottom)
# "V- Vertical (bottom to top)
# "D1" Diagonal (top-left to bottom-right)
# "D1" Diagonal (bottom-right to top-left)
# "D2" Diagonal (top-right to bottom-left)
# "D2-" Diagonal (bottom-left to top-right)

# Examples:
# Input: prism_detector(["ABC", "DEF", "GHI"], "ADG")
# Output: [(0, 0, "V")]

# Input: prism_detector(["HELLO", "WORLD"], "LL")
# Output: [(0, 2, "H")]

# Input: prism_detector(["XYZ", "ABC", "DEF"], "XBF")
# Output: [(0, 0, "D1")]

# Input: prism_detector([], "ABC")
# Output:[]

# Input: prism_detector(["ABC"], "") pash-5.25°C
# pash-5.25

# D1

# )]

# bas

# Word Word

# Word

# 01-

# ((2,

# bash--

# Word/Ifor node in graph:


# Word/In

def prism_detector(grid: list[str], pattern: str) -> list[tuple[int, int, str]]:

    if not grid or not pattern:
        return []

    result = []

    directions = {
        "H": (0, 1),
        "H-": (0, -1),
        "V": (1, 0),
        "V-": (-1, 0),
        "D1": (1, 1),
        "D1-": (-1, -1),
        "D2": (1, -1),
        "D2-": (-1, 1)
    }

    for r in range(len(grid)):
        for c in range(len(grid[0])):

            for name in directions:

                dr, dc = directions[name]

                positions = []

                for i in range(len(pattern)):
                    positions.append(
                        (
                            r + i*dr,
                            c + i*dc
                        )
                    )

                if all(
                    0 <= x < len(grid)
                    and 0 <= y < len(grid[0])
                    and grid[x][y] == pattern[i]
                    for i, (x, y) in enumerate(positions)
                ):
                    result.append((r, c, name))

    return result

print(prism_detector(["ABC", "DEF", "GHI"], "ADG"))
print(prism_detector(["HELLO", "WORLD"], "LL"))
print(prism_detector(["XYZ", "ABC", "DEF"], "XBF"))