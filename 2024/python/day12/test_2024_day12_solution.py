from .solution import calculate_price


def test_solution():
    assert calculate_price("***") == 3
    assert calculate_price("*o") == 4
    assert calculate_price("o*") == 6
    assert calculate_price("*o*") == 5
    assert calculate_price("**o*") == 6
    assert calculate_price("o***") == 8
    assert calculate_price("*o@") == 94
    assert calculate_price("*#") == 49
    assert calculate_price("@@@") == 300
    assert calculate_price("#@") == 50
    assert calculate_price("#@Z") is None
