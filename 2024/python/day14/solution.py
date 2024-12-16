def min_moves_to_stables(reindeer, stables):
    r = sorted(reindeer)
    s = sorted(stables)
    m = 0
    for i, v in enumerate(r):
        m += abs(v - s[i])
    return m
