import re

while True:
    numbers = input("Введите числа через пробел: ")
    pattern = r"([^0-9\s]+|0\d+)"
    match = re.search(pattern, numbers)
    if numbers.count(" ") == 0 or match:
        print("Некорректный ввод!")
    else:
        break

myList = list(numbers.split())
print(myList)

result = list(filter(lambda num: False if len(num) != 2 else True, myList))

if len(result) == 0:
    print("Нет двухзначных чисел!")
print(" ".join(result))
