def calculate_discount(price, percent):
    if price < 0 or percent < 0:
        raise ValueError("Price and discount percentage must be non-negative")
    return price - (price * percent / 100)