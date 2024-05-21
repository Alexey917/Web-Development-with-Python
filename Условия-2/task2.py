firstNumber = int(input("Введите первое число: "))
secondNumber = int(input("Введите втрое число: "))
thirdNumber = int(input("Введите третье число: "))

maxNumber = 0
minNumber = 0
mid = 0

action = input("Укажите действие: вывести максимальное число, минимальное, среднеарифметическое ")

if action == "максимальное":
    maxNumber = max(firstNumber, secondNumber, thirdNumber)
    print(maxNumber)
elif action == "минимальное":
    minNumber = min(firstNumber, secondNumber, thirdNumber)
    print(minNumber)
elif action == "среднеарифметическое":
    mid = (firstNumber + secondNumber + thirdNumber) / 3
    print(mid)
else:
    print("такое действие не предусмотрено")