meters = int(input("Метров "))



action = input("Укажите действие: перевести метры в: мили, дюймы, ярды\n")

if action == "мили":
    mile = meters / 160934
    print(mile)
elif action == "дюймы":
    inch = meters * 39.37
    print(inch)
elif action == "ярды":
    yards = meters * 1.094
    print(yards)
else:
    print("такое действие не предусмотрено")