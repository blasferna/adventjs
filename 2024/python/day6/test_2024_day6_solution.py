from .solution import in_box


def test_solution():
    assert in_box(["###", "#*#", "###"])
    assert in_box(["####", "#* #", "#  #", "####"])
    assert not in_box(["*####", "#   #", "#  #*", "####"])
    assert not in_box(["#####", "#   #", "#   #", "#   #", "#####"])
    assert in_box(["#####", "#   #", "# * #", "#   #", "#####"])
    assert in_box(["#####", "#   #", "#  *#", "#   #", "#####"])
    assert in_box(["#####", "#   #", "#   #", "#  *#", "#####"])
    assert not in_box(["#####", "#   #", "#   #", "#   #", "*#####"])
    assert not in_box(["#####", "#   #", "#   #", "#   #", "#####"])
    assert not in_box(["#*#", "###", "###"])
    assert not in_box(["###", "###", "#*#"])
    assert in_box(["###", "#*#", "###"])
    assert in_box(["####", "#* #", "#  #", "####"])
