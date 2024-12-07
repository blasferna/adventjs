from .solution import fix_packages


def test_solution():
    assert fix_packages("a(bc)de") == "acbde"
    assert fix_packages("a(cb)de") == "abcde"
    assert fix_packages("a(bc(def)g)h") == "agdefcbh"
    assert fix_packages("abc(def(gh)i)jk") == "abcighfedjk"
    assert fix_packages("a(b(c))e") == "acbe"
    assert fix_packages("a(b(c))e(za)") == "acbeaz"
