/**
 * @param {string[]} board - List of strings representing the board.
 * @param {"U" | "D" | "R" | "L"} mov - The movement direction.
 * @returns {"none" | "crash" | "eat"} - The resulting state of the train.
 */
function moveTrain(board, mov) {
    let state = "none";
    for (let i = 0; i < board.length; i++) {
        const row = board[i];
        const index = row.indexOf("@");
        if (index !== -1) {
            if (mov === "U") {
                if (i > 0) {
                    const prevRow = board[i - 1];
                    if (prevRow[index] === "*") return "eat";
                    if (prevRow[index] === "·") return "none";
                }
                if (i === 0) return "crash";
            }
            if (mov === "D") {
                if (i + 1 < board.length) {
                    const nextRow = board[i + 1];
                    if (nextRow[index] === "o") return "crash";
                    if (nextRow[index] === "*") return "eat";
                    if (nextRow[index] === "·") return "none";
                }
            }
            let movement = mov === "L" ? -1 : 1;
            if (mov === "L") {
                if (index === 0) return "crash";
                if (row[index - 1] === "*") return "eat";
                if (row[index - 1] === "o") return "crash";
                if (row[index - 1] === "·") return "none";
            }
            if (mov === "R") {
                if (index + 1 === row.length) return "crash";
                if (row[index + 1] === "*") return "eat";
                if (row[index + 1] === "o") return "crash";
                if (row[index + 1] === "·") return "none";
            }
        }
    }
    return state;
}
