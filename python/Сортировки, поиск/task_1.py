import random

li_1 = []
li_2 = []
li_3 = []
li_4 = []
li_5 = []

for i in range(5):
    li_1.append(random.randint(1, 250))
    li_2.append(random.randint(1, 250))
    li_3.append(random.randint(1, 250))
    li_4.append(random.randint(1, 250))

li_5 = li_1 + li_2 + li_3 + li_4

print(li_1)
print(li_2)
print(li_3)
print(li_4)
print(li_5)

print("\nКак бы вы хотели отсортировать список? Выберите a - по убыванию, b - по возрастанию")

while True:
    char = input()

    if char == "a":
        print("Сортировка по убыванию: ")
        # сортировка вставками
        i = 1
        while i < len(li_5):
            key = li_5[i]
            j = i - 1
            while li_5[j] < key and j >= 0:
                li_5[j + 1] = li_5[j]
                j -= 1
            li_5[j + 1] = key
            i += 1

        print(li_5)
        break
    elif char == "b":
        print("Сортировка по возрастанию: ")
        # пузырьковая сортировка
        i = 0
        while i < len(li_5):
            if li_5[i] > li_5[i + 1]:
                li_5[i], li_5[i + 1] = li_5[i + 1], li_5[i]
                i = 0
                continue
            i += 1
            if i == len(li_5)-1:
                break

        print(li_5)
        break
    else:
        print("или a или b: ")

print("\nПроверим есть ли число в списке")

try:
    numb = int(input("Введите число: "))
    if numb in li_5:
        print("Такое число есть в списке!: ")
    else:
        print("Такого числа нет в списке!: ")

except ValueError:
    print("Нужно ввести число! Попробуйте еще раз! ")


