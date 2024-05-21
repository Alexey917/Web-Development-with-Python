with open("files_for_tasks\\task_5.txt", encoding="utf-8") as file:
    date = file.read().split()
    print(date)
    count = 0
    find = input("Введите слово которое хотите найти: ")
    for word in range(len(date)):
        if date[word].lower() == find.lower():
            count += 1

    if count > 0:
        print(count)
    else:
        print("Нет такого слова")

