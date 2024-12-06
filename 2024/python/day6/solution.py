def in_box(box):
    i = 1
    for row in box:
        if i > 1 and i < len(box):
            if "*" in row:
                if row.find("*") not in [0, len(row)-1]:
                    return True
        i += 1
    return False
