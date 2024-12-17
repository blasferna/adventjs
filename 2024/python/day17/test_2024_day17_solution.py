from .solution import detect_bombs


def test_solution():
    assert detect_bombs(
        [[True, False, False], [False, True, False], [False, False, False]]
    ) == [[1, 2, 1], [2, 1, 1], [1, 1, 1]]
    assert detect_bombs([[True, False], [False, False]]) == [[0, 1], [1, 1]]
    assert detect_bombs([[True, True], [False, False], [True, True]]) == [
        [1, 1],
        [4, 4],
        [1, 1],
    ]
