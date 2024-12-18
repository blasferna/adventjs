from .solution import find_in_agenda


def test_solution():
    agenda = """+34-600-123-456 Calle Gran Via 12 <Juan Perez>
Plaza Mayor 45 Madrid 28013 <Maria Gomez> +34-600-987-654
<Carlos Ruiz> +1-800-555-0199 Fifth Ave New York"""
    assert find_in_agenda(agenda, "+34-600-123-456") == {
        "name": "Juan Perez",
        "address": "Calle Gran Via 12",
    }
