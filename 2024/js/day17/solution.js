function detectBombs(grid) {
    const result = grid.map(row => new Array(row.length).fill(0));

    for (let i = 0; i < grid.length; i++) {
        for (let j = 0; j < grid[i].length; j++) {
            let count = 0;

            if (i === 0) {
                if (j > 0 && grid[i][j - 1]) count++;
                if (j < grid[i].length - 1 && grid[i][j + 1]) count++;
                if (i < grid.length - 1) {
                    if (j > 0 && grid[i + 1][j - 1]) count++;
                    if (grid[i + 1][j]) count++;
                    if (j < grid[i].length - 1 && grid[i + 1][j + 1]) count++;
                }
            }
            else if (i === grid.length - 1) {
                if (j > 0 && grid[i][j - 1]) count++;
                if (j < grid[i].length - 1 && grid[i][j + 1]) count++;
                if (j > 0 && grid[i - 1][j - 1]) count++;
                if (grid[i - 1][j]) count++;
                if (j < grid[i].length - 1 && grid[i - 1][j + 1]) count++;
            }
            else {
                if (j === 0) {
                    if (grid[i][j + 1]) count++;
                    if (grid[i + 1][j]) count++;
                    if (grid[i + 1][j + 1]) count++;
                    if (grid[i - 1][j]) count++;
                    if (grid[i - 1][j + 1]) count++;
                }
                else if (j === grid[i].length - 1) {
                    if (grid[i][j - 1]) count++;
                    if (grid[i + 1][j]) count++;
                    if (grid[i + 1][j - 1]) count++;
                    if (grid[i - 1][j]) count++;
                    if (grid[i - 1][j - 1]) count++;
                }
                else {
                    if (grid[i][j - 1]) count++;
                    if (grid[i][j + 1]) count++;
                    if (grid[i + 1][j - 1]) count++;
                    if (grid[i + 1][j]) count++;
                    if (grid[i + 1][j + 1]) count++;
                    if (grid[i - 1][j - 1]) count++;
                    if (grid[i - 1][j]) count++;
                    if (grid[i - 1][j + 1]) count++;
                }
            }

            result[i][j] = count;
        }
    }
    return result;
}

const grid = [
    [false, true, false],
    [true, false, true],
    [false, true, false]
];

const result = detectBombs(grid);
console.log(result);
