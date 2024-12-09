from .solution import move_train


def test_solution():
    assert move_train(["·····", "*····", "@····", "o····", "o····"], "U") == "eat"
    assert move_train(["·····", "*····", "@····", "o····", "o····"], "D") == "crash"
    assert move_train(["·····", "*····", "@····", "o····", "o····"], "L") == "crash"
    assert move_train(["·····", "*····", "@····", "o····", "o····"], "R") == "none"
    assert move_train(["··@··", "··o··", "·*o··", "··o··", "··o··"], "U") == "crash"
