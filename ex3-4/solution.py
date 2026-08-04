def prism_detector(grid: list[str], pattern: str) -> list[tuple[int, int, str]]:
    if not grid or not pattern:
        return []

    directions = [
        (0, 1, "H"), (0, -1, "H-"),
        (1, 0, "V"), (-1, 0, "V-"),
        (1, 1, "D1"), (-1, -1, "D1-"),
        (1, -1, "D2"), (-1, 1, "D2-"),
    ]

    rows = len(grid)
    result = []

    for r in range(rows):
        for c in range(len(grid[r])):
            for dr, dc, code in directions:
                for k, ch in enumerate(pattern):
                    rr, cc = r + dr * k, c + dc * k
                    if not (0 <= rr < rows and 0 <= cc < len(grid[rr])) or grid[rr][cc] != ch:
                        break
                else:
                    result.append((r, c, code))

    return result


if __name__ == "__main__":
    print(prism_detector(["ABC", "DEF", "GHI"], "ADG"))
    print(prism_detector(["XYZ", "ABC", "DEF"], "XBF"))
    print(prism_detector([], "ABC"))
