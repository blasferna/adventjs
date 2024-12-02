def createFrame(names):
    max_length = max([len(x) for x in names])
    border = "*" * (max_length + 4)
    frame = border + "\n"

    for name in names:
        frame += f"* {name:<{max_length}} *\n"

    frame += border

    return frame
