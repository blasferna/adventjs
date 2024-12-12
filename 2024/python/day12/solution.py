def calculate_price(ornaments: str) -> int:
    prices = {"*": 1, "o": 5, "^": 10, "#": 50, "@": 100}
    ornaments_prices = []
    for char in ornaments:
        if char not in prices:
            return None
        ornaments_prices.append(prices[char])
    i = 0
    for price in ornaments_prices:
        if i + 1 < len(ornaments_prices):
            if price < ornaments_prices[i + 1]:
                ornaments_prices[i] = price * -1
        i += 1
    return sum(ornaments_prices)
