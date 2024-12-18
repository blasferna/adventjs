def find_in_agenda(agenda: str, phone: str) -> dict | None:
    kids = agenda.split("\n")
    kid = [kid for kid in kids if phone in kid]
    if kid and len(kid) == 1:
        name = kid[0].split("<")[1].split(">")[0]
        address = kid[0].split(" ")[1:-1]
        address = " ".join(address).split("<")[0].strip()
        return {"name": name, "address": address}
    return None


agenda = """+34-600-123-456 Calle Gran Via 12 <Juan Perez>
Plaza Mayor 45 Madrid 28013 <Maria Gomez> +34-600-987-654
<Carlos Ruiz> +1-800-555-0199 Fifth Ave New York"""
print(find_in_agenda(agenda, "1"))
