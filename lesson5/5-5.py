a = [1,2,3]
b = a.copy()

b.remove(3) # index 아니고 value
b.append(5)

print(a)
print(b)


names = ["Maya", "John", "Sarah", "Alex", "Maya","Jina"]
print(names.count("Maya"))
print(names.index("Maya")) # 첫번째 Maya의 index

numbers = [4,7,9,3,3,7,3,1,9]
numbers.sort() # 1부터
numbers.reverse() # 9부터

