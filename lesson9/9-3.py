def add_all(*args):
    total = 0
    for n in args:
        total = total + n
    return total

print(add_all(1,2,5,4,7,8,6,25,78,90))

def print_profile(**kwargs):
    for key in kwargs:
        print(key, "=", kwargs[key])

print_profile(name = "Jiyun", city = "New York", fruit = "Apple")