from .solution import draw_race


def test_solution():
    expected = """  ~~~~~~~~~~ /1
 ~~~~~r~~~~ /2
~~~~~~~r~~ /3"""

    assert draw_race([0, 5, -3], 10) == expected
