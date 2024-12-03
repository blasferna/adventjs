from .solution import organizeInventory


def test_solution():
    assert organizeInventory([]) == {}

    inventory = [
        {"name": "doll", "quantity": 5, "category": "toys"},
        {"name": "car", "quantity": 3, "category": "toys"},
        {"name": "ball", "quantity": 2, "category": "sports"},
        {"name": "car", "quantity": 2, "category": "toys"},
        {"name": "racket", "quantity": 4, "category": "sports"},
    ]
    expected = {"toys": {"doll": 5, "car": 5}, "sports": {"ball": 2, "racket": 4}}
    assert organizeInventory(inventory) == expected

    inventory = [
        {"name": "book", "quantity": 10, "category": "education"},
        {"name": "book", "quantity": 5, "category": "education"},
        {"name": "paint", "quantity": 3, "category": "art"},
    ]
    expected = {"education": {"book": 15}, "art": {"paint": 3}}
    assert organizeInventory(inventory) == expected

    inventory = [{"name": "pen", "quantity": 1, "category": "office"}]
    expected = {"office": {"pen": 1}}
    assert organizeInventory(inventory) == expected

    inventory = [
        {"name": "laptop", "quantity": 2, "category": "electronics"},
        {"name": "phone", "quantity": 3, "category": "electronics"},
        {"name": "desk", "quantity": 1, "category": "furniture"},
        {"name": "chair", "quantity": 4, "category": "furniture"},
        {"name": "phone", "quantity": 2, "category": "electronics"},
    ]
    expected = {
        "electronics": {"laptop": 2, "phone": 5},
        "furniture": {"desk": 1, "chair": 4},
    }
    assert organizeInventory(inventory) == expected

    inventory = [
        {"name": "paper", "quantity": 0, "category": "office"},
        {"name": "pencil", "quantity": 0, "category": "office"},
    ]
    expected = {"office": {"paper": 0, "pencil": 0}}
    assert organizeInventory(inventory) == expected
