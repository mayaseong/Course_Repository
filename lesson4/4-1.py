range(5) # 0,1,2,3,4
range(1,5) # 1,2,3,4
range(1,10,2) # 1,3,5,7,9

for i in range(5):
    print(i)

for num in range(1,5):
    print("Attempt: ", num)


total = 0

for i in range(1,10,3):
    total += i
    print(total)

for i in range(6):
    if i == 4:
        break
    print(i) # 0,1,2,3

for i in range(6):
    print(i) #0,1,2,3,4
    if i == 4:
        break 


for i in range(6):
    if i == 4:
        continue
    print(i) # 0,1,2,3,5

for i in range(6):
    print(i)
    if i == 4:
        continue
    # This will print 0 to 5 