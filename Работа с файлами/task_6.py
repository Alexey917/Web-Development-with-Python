with open("files_for_tasks\\task_6.txt", "r+", encoding="utf-8") as file:
    date = file.read().split()
    search = input("Введите слово которое хотите найти: ")
    replace = input("Введите слово для замены: ")
    count = 0
    for word in range(len(date)):
        if search.lower() == date[word].lower():
            date[word] = replace
            count += 1

    while True:
        if count > 0:
            print(date)
            break
        else:
            print("Нет такого слова")
            print("Нет такого слова")
            search = input("Введите слово которое хотите найти: ")
            replace = input("Введите слово для замены: ")

    for word in range(len(date)):
        if word == len(date) - 1:
            break
        date[word] += " "

    date[4] += "\n"
    date[9] += "\n"
    date[12] += "\n"
    date[17] += "\n"
    date[21] += "\n"
    file.seek(0)
    file.writelines(date)

