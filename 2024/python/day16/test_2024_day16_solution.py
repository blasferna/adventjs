from .solution import remove_snow

def test_solution():
    assert remove_snow("zxxzoz") == "oz"
    assert remove_snow("abcdd") == "abc"
    assert remove_snow("zzz") == "z"
    assert remove_snow("a") == "a"
