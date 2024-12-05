def organizeShoes(shoes):
    boots = []
    temp = []
    for shoe in shoes:
        search_type = "I" if shoe["type"] == "R" else "R"
        other_side = f"{search_type}{shoe['size']}"
        curr_side = f"{shoe['type']}{shoe['size']}" 
        if other_side in temp:
            boots.append(shoe["size"])
            temp.remove(other_side)
        else:
            temp.append(curr_side)
    return boots
