def draw_race(indices, length):
    tracks = []
    gap = len(indices) - 1
    line = 1
    for index in indices:
        track = "" + " " * gap
        if index < 0:
            index = length + index
        for i in range(length):
            if i == index and index != 0:
                track += "r"
            else:
                track += "~"
        gap -= 1
        tracks.append(f"{track} /{line}")
        line += 1
    return '\n'.join(tracks)
