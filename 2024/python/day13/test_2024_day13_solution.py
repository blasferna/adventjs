from .solution import is_robot_back


def test_solution():
    assert is_robot_back("R") == [1, 0]
    assert is_robot_back("RL")
    assert is_robot_back("RLUD")
    assert is_robot_back("*RU") == [2, 1]
    assert is_robot_back("R*U") == [1, 2]
    assert is_robot_back("LLL!R") == [-4, 0]
    assert is_robot_back("R?R") == [1, 0]
    assert is_robot_back("U?D")
    assert is_robot_back("R!L") == [2, 0]
    assert is_robot_back("U!D") == [0, 2]
    assert is_robot_back("R?L")
    assert is_robot_back("U?U") == [0, 1]
    assert is_robot_back("*U?U") == [0, 2]
    assert is_robot_back("U?D?U")
    assert is_robot_back("R!U?U") == [1, 0]
