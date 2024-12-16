def remove_snow(s: str) -> str:
    clean = True
    while clean:
        previous = ""
        to_clean = ""
        for char in s:
            if previous == char:
                to_clean = previous + char
                break
            previous = char
        if to_clean:
            s = s.replace(to_clean, "")
        else:
            clean = False
    return s


print(remove_snow("zxxzoz"))
