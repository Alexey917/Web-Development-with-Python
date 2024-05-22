import json


class Number:
    def __init__(self):
        self.number = 45
        self.oct = 8
        self.hex = 16
        self.bin = 2
        self.path = 'number.txt'

    def write_and_read(self):
        if self.path == 'number.txt':
            with open(self.path, 'w') as f:
                json.dump(self.number, f)
        else:
            raise FileNotFoundError(f'Неверно указан путь!')

        with open(self.path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            print(f'Данные из файла: {data}')

    def conversion(self, num_sys):
        num = self.number
        remainder = []  # остаток
        while True:
            if num % num_sys == 10:
                remainder.append("A")
            elif num % num_sys == 11:
                remainder.append("B")
            elif num % num_sys == 12:
                remainder.append("C")
            elif num % num_sys == 13:
                remainder.append("D")
            elif num % num_sys == 14:
                remainder.append("E")
            elif num % num_sys == 15:
                remainder.append("F")
            else:
                remainder.append(str(num % num_sys))
            num = num // num_sys
            if num == 0:
                break
        res = ''.join(remainder[::-1])
        print(f'результат перевода числа в восьмеричную систему исчисления: {res}')
        return res


# def get_menu():
#     while True:
#         menu = input("Выберите действие: \n"
#                      "----------------------------------------\n"
#                      "1-Запись и чтение значения\n"
#                      "2-Перевод числа в восьмеричную систему исчисления\n"
#                      "3-Перевод числа в шестнадцатеричную систему исчисления\n"
#                      "4-Перевод числа в двоичную систему исчисления\n"
#                      "5-Выход из меню\n"
#                      "----------------------------------------"
#                      "\n-> ")
#
#         match menu:
#             case "1":
#                 number.write_and_read()
#             case "2":
#                 number.conversion(number.oct)
#             case "3":
#                 number.conversion(number.hex)
#             case "4":
#                 number.conversion(number.bin)
#             case "5":
#                 break
#             case _:
#                 print(f'Нет такого пункта меню!')


number = Number()
# get_menu()
number.write_and_read()
number.conversion(number.oct)
number.conversion(number.hex)
number.conversion(number.bin)

