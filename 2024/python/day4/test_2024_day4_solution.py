from .solution import createXmasTree


def test_solution():
    ornament = "*"
    height = 5
    expected = """____*____
___***___
__*****__
_*******_
*********
____#____
____#____"""

    assert createXmasTree(ornament, height) == expected


    ornament = "+"
    height = 3
    expected = """__+__
_+++_
+++++
__#__
__#__"""
    
    assert createXmasTree(ornament, height) == expected


    ornament = "@"
    height = 6
    expected = """_____@_____
____@@@____
___@@@@@___
__@@@@@@@__
_@@@@@@@@@_
@@@@@@@@@@@
_____#_____
_____#_____"""
