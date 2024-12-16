from .solution import min_moves_to_stables


def test_solution():
    assert min_moves_to_stables([2, 6, 9], [3, 8, 5]) == 3
    assert min_moves_to_stables([1, 1, 3], [1, 8, 4]) == 8
