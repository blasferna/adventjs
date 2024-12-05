from .solution import organizeShoes


def test_solution():
    shoes = [
        {"type": "I", "size": 38},
        {"type": "R", "size": 38},
        {"type": "R", "size": 42},
        {"type": "I", "size": 41},
        {"type": "I", "size": 42},
    ]
    expected = [38, 42]
    assert organizeShoes(shoes) == expected

    shoes = [
        {"type": "I", "size": 38},
        {"type": "R", "size": 38},
        {"type": "I", "size": 38},
        {"type": "I", "size": 38},
        {"type": "R", "size": 38},
    ]
    expected = [38, 38]
    assert organizeShoes(shoes) == expected

    shoes = [
        {"type": "I", "size": 38},
        {"type": "R", "size": 36},
        {"type": "R", "size": 42},
        {"type": "I", "size": 41},
        {"type": "I", "size": 43},
    ]
    expected = []
    assert organizeShoes(expected) == []
