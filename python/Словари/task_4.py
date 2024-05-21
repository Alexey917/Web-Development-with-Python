book_collection = [
    {
        "автор": "Джеймс Клир",
        "название книги": "Атомные привычки",
        "жанр": "Психология",
        "год выпуска": "2019",
        "количество страниц": "304",
        "издательство": "Питер",
    },

    {
        "автор": "Питер Уоттс",
        "название книги": "Эхопраксия",
        "жанр": "Научная фантастика",
        "год выпуска": "2021",
        "количество страниц": "480",
        "издательство": "Астрель",
    },

    {
        "автор": "Александр Волков",
        "название книги": "Искусственный интеллект. От компьютеров к киборгам",
        "жанр": "Естественные науки",
        "год выпуска": "2020",
        "количество страниц": "256",
        "издательство": "Вече",
    },

    {
        "автор": "Хауи Хью",
        "название книги": "Укрытие. Книга 1. Иллюзия",
        "жанр": "Фантастика",
        "год выпуска": "2023",
        "количество страниц": "544",
        "издательство": "Азбука",
    }
]


def add_book(lst):
    dictionary = {
        "автор": "",
        "название книги": "",
        "жанр": "",
        "год выпуска": "",
        "количество страниц": "",
        "издательство": "",
    }

    for key, value in dictionary.items():
        value = input(key + ":\t")
        dictionary[key] = value.lower()

    lst.append(dictionary)

    return output_books(book_collection)


def delete_book(lst, count):
    name_book = input("Введите название книги: ")
    for i in lst:
        for key, value in i.items():
            count += 1
            if name_book.lower() == i[key].lower():
                lst.remove(i)
                return output_books(book_collection)
    if count // 6 == len(lst):
        print("Нет такой книги в нашей коллекции!")
        return -1


def search_book(lst, count):
    name_book = input("Введите название книги: ")
    for i in lst:
        for key, value in i.items():
            count += 1
            if name_book.lower() == i[key].lower():
                return i
    if count // 6 == len(lst):
        print("Нет такой книги в нашей коллекции!")
        return -1


def replace_book(lst, count):
    name_book = input("Введите название книги: ")
    update_key = input("Введите информацию для обновления: ")
    update_val = input("Укажите на что будет изменено значение: ")
    for i in lst:
        for key, value in i.items():
            count += 1
            if name_book.lower() == i[key].lower():
                i[update_key.lower()] = update_val.lower()
                return i
    if count // 6 == len(lst):
        print("Нет такой книги в нашей коллекции!")
        return -1


def output_books(lst):
    for i in lst:
        for key, value in i.items():
            print(key, ":", value)
        print(end="\n")


while True:
    menu = input("Выберите действие: "
                 "1-добавить книгу, "
                 "2-удалить книгу, "
                 "3-поиск книги, "
                 "4-Обновление данных по книге, "
                 "5-выход из меню\n")

    match menu:
        case "1":
            add_book(book_collection)
        case "2":
            delete_book(book_collection, 0)
        case "3":
            print(search_book(book_collection, 0))
        case "4":
            print(replace_book(book_collection, 0))
        case "5":
            break







