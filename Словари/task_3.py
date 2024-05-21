person = {
    "full_name": "",
    "telephone": "",
    "email": "",
    "job_title": "",
    "office_number": "",
    "skype": "",
}

print("Заполните информацию о сотруднике: ")


def filling(dictionary):
    for key, value in dictionary.items():
        value = input(key + "\t")
        dictionary[key] = value
    return dictionary


print(filling(person))


def deletion(dictionary, counter):
    val = input("Введите данные для удаления: ")
    while True:
        for key, value in dictionary.items():
            counter += 1
            if val == key or val == dictionary[key]:
                dictionary.pop(key)
                return dictionary
        if counter == len(dictionary):
            print("Нет таких данных о сотруднике!")
            return -1


print(deletion(person, 0))


def search(dictionary, counter):
    val = input("Введите данные для поиска: ")
    while True:
        for key in dictionary.keys():
            counter += 1
            if val == key:
                return dictionary.get(key)
        if counter == len(dictionary):
            print("Нет таких данных о сотруднике!")
            return -1


print(search(person, 0))


def replacement(dictionary, counter):
    update_key = input("Введите данные, которые нужно заменить: ")
    val = input("Введите новое значение ключа: ")
    while True:
        for key in dictionary.keys():
            counter += 1
            if update_key == key:
                dictionary.update({key: val})
                return dictionary
        if counter == len(dictionary):
            print("Нет таких данных о сотруднике!")
            return -1


print(replacement(person, 0))


