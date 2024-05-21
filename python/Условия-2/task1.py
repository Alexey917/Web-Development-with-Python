firstNumber = int(input("Введите первое число: "))
secondNumber = int(input("Введите втрое число: "))
thirdNumber = int(input("Введите третье число: "))

sum = 0
mult = 0

action = input("Укажите действие сложение или умножение: ")

if action == "сложение":
    sum = firstNumber + secondNumber + thirdNumber
    print(sum)
elif action == "умножение":
    mult = firstNumber * secondNumber * thirdNumber
    print(mult)
else:
    print("такое действие не предусмотрено")