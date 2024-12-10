from .solution import compile


def test_solution():
    instructions = ["MOV -1 C", "INC C", "JMP C 1", "MOV C A", "INC A"]

    assert compile(instructions) == 2
