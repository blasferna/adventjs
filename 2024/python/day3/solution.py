from collections import defaultdict


def organizeInventory(inventory):
    organized = defaultdict(lambda: defaultdict(int))
    for item in inventory:
        organized[item["category"]][item["name"]] += item["quantity"]
    return dict(organized)
