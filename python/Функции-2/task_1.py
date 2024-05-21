def nod_func(num1, num2):
    if num2 == 0:
        return num1
    else:
        return nod_func(num2, num1 % num2)


first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))

print(nod_func(first_number, second_number))


