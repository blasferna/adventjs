from .solution import prepare_gifts


def test_2024_day1_solution():
    assert prepare_gifts([3, 1, 2, 3, 4, 2, 5]) == [1, 2, 3, 4, 5]
    assert prepare_gifts([6, 5, 5, 5, 5]) == [5, 6]
    assert prepare_gifts([]) == []
