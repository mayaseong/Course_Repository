def discounted_price(price, discount_percent):
    if price <= 0 or discount_percent <= 0:
        return None
    return price * (1 - discount_percent/100)

print(discounted_price(107, -1))
print(discounted_price(89, 7))
print(discounted_price(-299, 19))