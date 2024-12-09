from typing import List, Literal


def move_train(
    board: List[str], mov: Literal["U", "D", "R", "L"]
) -> Literal["none", "crash", "eat"]:
    i = 0
    state = "none"
    for e in board:
        index = e.find("@")
        if index != -1:
            if mov == "U":
                if i > 0:
                    prev = board[i - 1]
                    if prev[index] == "*":
                        return "eat"
                    if prev[index] == "·":
                        return "none"
                if i == 0:
                    return "crash"
            if mov == "D":
                if i + 1 < len(board):
                    next = board[i + 1]
                    if next[index] == "o":
                        return "crash"
                    if next[index] == "*":
                        return "eat"
                    if next[index] == "·":
                        return "none"
            if mov == "L":
                if index == 0:
                    return "crash"
                if e[index - 1] == "*":
                    return "eat"
                if e[index - 1] == "o":
                    return "crash"
                if e[index - 1] == ".":
                    return "none"
            if mov == "R":
                if index + 1 == len(e):
                    return "crash"
                if e[index + 1] == "*":
                    return "eat"
                if e[index + 1] == "o":
                    return "crash"
                if e[index + 1] == "·":
                    return "none"
        i += 1
    return state


if __name__ == "__main__":
    print(move_train(["··@··", "··o··", "·*o··", "··o··", "··o··"], "U"))
