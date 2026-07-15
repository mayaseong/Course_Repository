def is_passing(score):
    return score >=60

print(is_passing(61))
print(is_passing(59))


def safe_divide(a, b):
    if b == 0 :
        return None
    else:
        return round(a/b, 4)
    
print(safe_divide(4,7))
print(safe_divide(6,0))