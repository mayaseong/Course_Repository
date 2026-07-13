counter = 0

while counter < 5:
    print(counter)
    counter += 1


names = ["Maya", "John", "Sarah", "Alex"]

for name in names:
    print(name)

numbers = [2,5,8,4,9,1]
count = 0
sum = 0
found = 0

for number in numbers:
    if number >= 5:
        count += 1

print(count)

for number in numbers:
    sum += number
    
print(sum)

for number in numbers:
    if number%2 == 1:
        found += 1

print(found)