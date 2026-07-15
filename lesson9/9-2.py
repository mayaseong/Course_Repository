def compute_tax_and_total(price, tax_rate):
    tax = price * tax_rate
    total = price + tax
    return round(tax, 3), round(total, 3)

tx, tl = compute_tax_and_total(56, 0.08)
print(tx)
print(tl)

tl, tx = compute_tax_and_total(56, 0.08)
print(tx)
print(tl)