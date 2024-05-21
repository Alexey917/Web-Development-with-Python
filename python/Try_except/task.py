import re

expression = input("Введите арифметическое выражение: ")

numbers = re.findall(r'\d+', expression)
print(numbers)

try:
    operator = re.search(r'([+\-*/])', expression)
    print(operator.group(0))

    if operator.group(0) == "+":
        result = int(numbers[0]) + int(numbers[1])
        print(result)
    elif operator.group(0) == "-":
        result = int(numbers[0]) - int(numbers[1])
        print(result)
    elif operator.group(0) == "*":
        result = int(numbers[0]) * int(numbers[1])
        print(result)
    elif operator.group(0) == "/":
        result = int(numbers[0]) / int(numbers[1])
        print(result)

except Exception:
    print("Не предусмотренная операция")




