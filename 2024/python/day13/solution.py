def is_robot_back(moves: list[str]) -> bool | list[int]:
    modifiers = ["*", "!", "?"]
    commands = {
        "R": (0, 1, "L"),
        "L": (0, -1, "R"),
        "U": (1, 1, "D"),
        "D": (1, -1, "U"),
    }
    done = []
    modifier = None
    position = [0, 0]
    for i, mov in enumerate(moves):
        if mov in modifiers:
            modifier = mov
            continue
        command = mov
        if modifier:
            if modifier == "*":
                command = command * 2
            if modifier == "!":
                command = commands[mov][2]
            if modifier == "?":
                if command in done:
                    command = None
            modifier = None
        if command:
            for movement in command:
                index, increment, _ = commands[movement]
                position[index] = position[index] + increment
            done.append(command[0])
    if position == [0, 0]:
        return True
    return position
