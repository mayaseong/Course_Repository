def clean_name(name):
    cleaned = name.strip()
    return cleaned[0:1].upper() + cleaned[1:].lower()
    # 아니면 name.strip().capitalize() 써도됨

print(clean_name("mAYA     "))


raw_names = ["mAyA   ", "AvA ", "  DAVID ", "jinA"]
cleaned_names = [] #바뀐 이름 담을 새로운 list 제작
for name in raw_names:
    cleaned_names.append(clean_name(name))
    
print(cleaned_names)


def count_greater_than_threshold(numbers, threshold):
    count = 0
    for number in numbers:
        if number > threshold:
            count = count + 1
    return count   

numbers = [6,4,8,9,2]
print(count_greater_than_threshold(numbers, 5))