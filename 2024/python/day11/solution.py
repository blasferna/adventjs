def decode_filename(filename: str) -> str:
    left_part = filename.split("_")[0]
    right_part = filename.split(".")[-1]
    return filename.replace(f"{left_part}_", "").replace(f".{right_part}", "")
