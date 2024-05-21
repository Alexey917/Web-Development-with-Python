height = int(input("Введите высоту фигуры: "))
figure = input("Введите русскую букву от а-к: ")

if figure == "а":
    for i in range(height):
        print(" " * i+"*" * (height - i))

elif figure == "б":
    for i in range(height):
        print("*" * (i + 1)+" " * (height - i))

elif figure == "в":
    for i in range(height - 1, -1, -1):
        print(" " * (height - i)+"*" * (2 * i + 1))

    for i in range(height):
        print(" " * (height - i)+" " * (2 * i + 1))

elif figure == "г":
    for i in range(height - 1, -1, -1):
        print(" " * (height - i)+" " * (2 * i + 1))

    for i in range(height):
        print(" " * (height - i)+"*" * (2 * i + 1))

elif figure == "д":
    for i in range(height - 1, -1, -1):
        print(" " * (height - i)+"*" * (2 * i + 1))

    for i in range(height):
        print(" " * (height - i)+"*" * (2 * i + 1))

elif figure == "е":
    for i in range(height):
        print("*" * (i + 1)+" " * (height - i)+" " * (height - i)+"*" * (i + 1))
    for i in range(height-2, -1, -1):
        print("*" * (i + 1)+" " * (height - i)+" " * (height - i)+"*" * (i + 1))

elif figure == "ж":
    for i in range(height):
        print("*" * (i + 1)+" " * (height - i)+" " * (height - i)+" " * (i + 1))
    for i in range(height-2, -1, -1):
        print("*" * (i + 1)+" " * (height - i))

elif figure == "з":
    for i in range(height):
        print(" " * (i + 1)+" " * (height - i)+" " * (height - i)+"*" * (i + 1))
    for i in range(height-2, -1, -1):
        print(" " * (i + 1)+" " * (height - i)+" " * (height - i)+"*" * (i + 1))


elif figure == "и":
    for i in range(height):
        print("*" * (height - i)+" " * (i + 1))

elif figure == "к":
    for i in range(height):
        print(" " * (height - i)+"*" * (i + 1))
else:
    print("Нужно ввести русскую букву от а-к")