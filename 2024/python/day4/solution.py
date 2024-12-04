def createXmasTree(ornament, height):
    width = 1 + (height - 1) * 2
    branches = [f"{ornament * (1 + i*2):_^{width}}" for i in range(height)]
    trunk = [f"{'#':_^{width}}"] * 2
    return "\n".join(branches + trunk)
