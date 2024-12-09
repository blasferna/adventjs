from typing import List, Literal


def move_train(
    board: List[str], mov: Literal["U", "D", "R", "L"]
) -> Literal["none", "crash", "eat"]:
    movements = {
        "U": (-1, 0),
        "D": (1, 0),
        "L": (0, -1),
        "R": (0, 1),
    }

    head_x, head_y = None, None
    for i, row in enumerate(board):
        if "@" in row:
            head_x, head_y = i, row.index("@")
            break

    dx, dy = movements[mov]
    new_x, new_y = head_x + dx, head_y + dy

    if new_x < 0 or new_x >= len(board) or new_y < 0 or new_y >= len(board[0]):
        return "crash"

    next_cell = board[new_x][new_y]
    if next_cell == "o":
        return "crash"
    if next_cell == "*":
        return "eat"

    return "none"
