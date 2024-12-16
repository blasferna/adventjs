from .solution import draw_table


def test_solution():
    assert (
        draw_table(
            [
                {"name": "Alice", "city": "London"},
                {"name": "Bob", "city": "Paris"},
                {"name": "Charlie", "city": "New York"},
            ]
        )
        == """+---------+----------+
| Name    | City     |
+---------+----------+
| Alice   | London   |
| Bob     | Paris    |
| Charlie | New York |
+---------+----------+"""
    )

    assert (
        draw_table(
            [
                {"gift": "Doll", "quantity": 10},
                {"gift": "Book", "quantity": 5},
                {"gift": "Music CD", "quantity": 1},
            ]
        )
        == """+----------+----------+
| Gift     | Quantity |
+----------+----------+
| Doll     | 10       |
| Book     | 5        |
| Music CD | 1        |
+----------+----------+"""
    )

    assert (
        draw_table([{"name": "Alice", "city": "London"}])
        == """+-------+--------+
| Name  | City   |
+-------+--------+
| Alice | London |
+-------+--------+"""
    )

    assert (
        draw_table([{"id": 1, "score": 95}, {"id": 2, "score": 85}])
        == """+----+-------+
| Id | Score |
+----+-------+
| 1  | 95    |
| 2  | 85    |
+----+-------+"""
    )
