def detect_bombs(grid: list[list[bool]]) -> list[list[int]]:
    result = [[0 for _ in range(len(row))] for row in grid]

    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            count = 0

            if i == 0:
                if j > 0:
                    if grid[i][j - 1]:
                        count += 1
                if j < len(row) - 1:
                    if grid[i][j + 1]:
                        count += 1
                if i < len(grid) - 1:
                    if j > 0:
                        if grid[i + 1][j - 1]:
                            count += 1
                    if grid[i + 1][j]:
                        count += 1
                    if j < len(row) - 1:
                        if grid[i + 1][j + 1]:
                            count += 1

            elif i == len(grid) - 1:
                if j > 0:
                    if grid[i][j - 1]:
                        count += 1
                if j < len(row) - 1:
                    if grid[i][j + 1]:
                        count += 1
                if j > 0:
                    if grid[i - 1][j - 1]:
                        count += 1
                if grid[i - 1][j]:
                    count += 1
                if j < len(row) - 1:
                    if grid[i - 1][j + 1]:
                        count += 1

            else:
                if j == 0:
                    if grid[i][j + 1]:
                        count += 1
                    if grid[i + 1][j]:
                        count += 1
                    if grid[i + 1][j + 1]:
                        count += 1
                    if grid[i - 1][j]:
                        count += 1
                    if grid[i - 1][j + 1]:
                        count += 1

                elif j == len(row) - 1:
                    if grid[i][j - 1]:
                        count += 1
                    if grid[i + 1][j]:
                        count += 1
                    if grid[i + 1][j - 1]:
                        count += 1
                    if grid[i - 1][j]:
                        count += 1
                    if grid[i - 1][j - 1]:
                        count += 1

                else:
                    if grid[i][j - 1]:
                        count += 1
                    if grid[i][j + 1]:
                        count += 1
                    if grid[i + 1][j - 1]:
                        count += 1
                    if grid[i + 1][j]:
                        count += 1
                    if grid[i + 1][j + 1]:
                        count += 1
                    if grid[i - 1][j - 1]:
                        count += 1
                    if grid[i - 1][j]:
                        count += 1
                    if grid[i - 1][j + 1]:
                        count += 1

            result[i][j] = count
    return result
