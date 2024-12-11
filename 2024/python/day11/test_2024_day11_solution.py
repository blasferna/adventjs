from .solution import decode_filename


def test_solution():
    assert decode_filename('2023122512345678_sleighDesign.png.grinchwa') == "sleighDesign.png"
    assert decode_filename('42_chimney_dimensions.pdf.hack2023') == "chimney_dimensions.pdf"
    assert decode_filename('987654321_elf-roster.csv.tempfile') == "elf-roster.csv"
