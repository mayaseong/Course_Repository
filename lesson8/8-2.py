def compute_total(price, tax_rate):
    pre_total = price * (1 + tax_rate)
    total = round(pre_total, 3)
    return total
    #or tax = price * tax_rate
    # total = price + tax

print(compute_total(100, 0.09))
print(compute_total(price = 99, tax_rate = 0.065))