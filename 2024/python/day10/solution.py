def compile(instructions):
    pointer = 0
    registry = {}

    while pointer < len(instructions):
        instruction = instructions[pointer]
        params = instruction.split(" ")
        action = params[0]
        x = params[1]
        y = None if len(params) <= 2 else params[2]
        if action == "MOV":
            registry[y] = registry[x] if x in registry else int(x)
            pointer += 1
        if action == "INC":
            registry[x] = registry.get(x, 0) + 1
            pointer += 1
        if action == "DEC":
            registry[x] = registry.get(x, 0) - 1
            pointer += 1
        if action == "JMP":
            if x not in registry:
                registry[x] = 0
            value = registry[x]
            if value == 0:
                pointer = int(y)
            else:
                pointer += 1
    return  registry.get("A")

