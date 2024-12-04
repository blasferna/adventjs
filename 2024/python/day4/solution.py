def createXmasTree(ornament, height):
    width = 1 + (height - 1) * 2
    branches = [(ornament * (1 + i * 2)).center(width, "_") for i in range(height)]
    trunk = ["#".center(width, "_")] * 2
    return '\n'.join(branches + trunk)
