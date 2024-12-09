/**
 * @param {string[]} board - List of strings representing the board.
 * @param {"U" | "D" | "R" | "L"} mov - The movement direction.
 * @returns {"none" | "crash" | "eat"} - The resulting state of the train.
 */
function moveTrain(board, mov) {
  const movements = {
    U: [-1, 0],
    D: [1, 0],
    L: [0, -1],
    R: [0, 1],
  };

  let headX = null,
    headY = null;

  for (let i = 0; i < board.length; i++) {
    const row = board[i];
    const index = row.indexOf("@");
    if (index !== -1) {
      headX = i;
      headY = index;
      break;
    }
  }

  const [dx, dy] = movements[mov];
  const newX = headX + dx;
  const newY = headY + dy;

  if (newX < 0 || newX >= board.length || newY < 0 || newY >= board[0].length) {
    return "crash";
  }

  const nextCell = board[newX][newY];

  if (nextCell === "o") {
    return "crash";
  }
  if (nextCell === "*") {
    return "eat";
  }

  return "none";
}
