import re


class Dictionary:
    def __init__(self):
        self.dictionary = {
            "react to: ": "",
            "somehow: ": "",
            "point at: ": "",
            "forever: ": "",
            "available: ": "",
            "notice: ": "",
            "threat: ": "",
        }

        self.correct_translation = {
            "react to: ": "реагировать на",
            "somehow: ": "как то",
            "point at: ": "указывать на",
            "forever: ": "вечно",
            "available: ": "доступен",
            "notice: ": "заменить",
            "threat: ": "угроза",
        }

    def filling(self):
        for key, value in self.dictionary.items():
            value = input("Переведите" + " " + key)
            self.dictionary[key] = value

    def check_correct_filling(self):
        pattern = r'[a-zA-Z\d!@#№$%^&*()\-\_+=:;\"\'\\|\?/><.<`~]+'

        print(end="\n")
        for key, value in self.dictionary.items():
            search = re.search(pattern, value)

            while search:
                print("Перевод должен быть на русском языке! Не содержать цифры и спец.символы!")
                value = input("Переведите " + key + "еще раз!: ")
                search = re.search(pattern, value)

                if not search:
                    self.dictionary.update({key: value})
                    break

        print(end="\n")
        for key, value in self.dictionary.items():
            print(key, value)

    def add_elements(self):
        key = input("Введите слово на английском: ")
        value = input("Введите слово на русском: ")
        self.correct_translation[key] = value.lower()
        return self.correct_translation

    def deletion(self, counter):
        for key, value in self.correct_translation.items():
            if key in self.dictionary:
                if self.dictionary[key].lower() == value:
                    counter += 1
                else:
                    self.dictionary.pop(key)
        print("Правильно переведено " + str(counter) + " слов(а)")
        return self.dictionary

    def search(self):
        word = input("Введите слово для поиска. Если это английское слово, то в конце укажите : иначе ничего не найдет\n")
        pattern = r'[a-zA-Z\d!@#№$%^&*()\-\_+=:;\"\'\\|\?/><.<`~]+'
        pattern2 = r'[а-яА-Я\d!@#№$%^&*()\-\_+=:;\"\'\\|\?/><.<`~]+'
        match = re.search(pattern, word)
        match2 = re.search(pattern2, word)
        if not match:
            for key, value in self.correct_translation.items():
                if value == word:
                    return key
            print("В словаре нет такого слова")
        if not match2:
            for key in self.correct_translation.keys():
                if key == word:
                    return self.correct_translation.get(key)
            print("В словаре нет такого слова")


obj_dictionary = Dictionary()
print("Заполнение словаря: ")
obj_dictionary.filling()

print("Проверка правильности заполнения словаря: ")
obj_dictionary.check_correct_filling()

print("\nПроверка на правильность перевода и удаление не верных вариантов: ")
print(obj_dictionary.deletion(0))

print("\nПоиск по словарю: ")
print(obj_dictionary.search())

print("\nДобавление нового слова в словарь: ")
print(obj_dictionary.add_elements())

