def compile(instructions):
    position = 0
    vars = {}

    while position < len(instructions):
        instruction = instructions[position]
        params = instruction.split(" ")
        action = params[0]
        x = params[1]
        y = None
        if len(params) > 2:
            y = params[2]
        if action == "MOV":
            vars[y] = vars[x] if x in vars else int(x)
            position += 1
        if action == "INC":
            vars[x] += 1
            position += 1
        if action == "JMP":
            value = vars.get(x, 0)
            if value == 0:
                position = int(y)
            else:
                position += 1
    return vars.get("A", "undefined")
