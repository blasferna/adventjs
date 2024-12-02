from .solution import createFrame


def test_solution():
    expected = """***************
* midu        *
* madeval     *
* educalvolpz *
***************"""
    assert createFrame(["midu", "madeval", "educalvolpz"]) == expected

    expected = """********
* midu *
********"""

    assert createFrame(["midu"]) == expected

    EXPECTED = """*******
* a   *
* bb  *
* ccc *
*******"""

    assert createFrame(["a", "bb", "ccc"]) == EXPECTED
