while True:
    string = input("Введите название городов через пробел: ")
    if string.count(" ") == 0:
        print("Некорректный ввод!")
    else:
        break

myList = list(string.split())
print(myList)

resultString = list(filter(lambda string1: False if len(string1) < 5 else True, myList))

if len(resultString) == 0:
    print("Нет городов с названиями менее 5 символов!")
print(" ".join(resultString))
#Moscow Penza Yalta Sochi Piter Novgorod Archangelsk