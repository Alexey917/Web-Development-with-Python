import re


class User:
    def __init__(self):
        self.__login = None
        self.__password = None
        self.next = None
        self.prev = None

    @property
    def login(self):
        return self.__login

    @login.setter
    def login(self, login):
        self.__login = login

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password


class UserList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_user(self):
        user = User()
        user.login = input("Введите имя пользователя -> ")
        if not UserList.verify_login(user.login):
            return False
        if self.check_user_for_other_func(user.login):
            return False
        user.password = input("Введите пароль -> ")
        if not UserList.verify_password(user.password):
            return False
        if self.head is None:
            self.head = user
            self.tail = user
        else:
            ptr = user
            ptr.prev = self.tail
            ptr = ptr.prev
            ptr.next = user
            self.tail = user

        self.display_users()
        print("\n")

    def delete_user(self):
        if self.head is None:
            print("Список пользователей пуст. Удалять некого.\n")
            return False
        else:
            name = input("Укажите пользователя, которого нужно удалить: ")
            if not UserList.verify_login(name):
                return False
            if self.check_user_for_other_func(name):
                ptr = self.head
                while ptr is not None:
                    if ptr == self.head and ptr.login == name and ptr != self.tail:
                        left = ptr
                        ptr = ptr.next
                        left.next = None
                        ptr.prev = None
                        self.head = ptr
                        del left
                        break
                    if ptr == self.head and ptr.login == name and ptr == self.tail:
                        self.head = None
                        self.tail = None
                        del ptr
                        print("Список пользователей пуст.")
                        break
                    if ptr.login == name:
                        right = ptr.next
                        left = ptr.prev
                        left.next = right
                        right.prev = left
                        temp = ptr
                        ptr = right
                        temp.next = None
                        temp.prev = None
                        del temp
                        break
                    if ptr.next == self.tail and self.tail.login == name:
                        right = self.tail
                        right.prev = None
                        ptr.next = None
                        self.tail = ptr
                        del right
                        break
                    ptr = ptr.next
        self.display_users()
        print("\n")

    def check_user(self):
        name = input("Введите имя пользователя(login): ")
        if not UserList.verify_login(name):
            return False
        ptr = self.head
        while ptr is not None:
            if name == ptr.login:
                print("Такой пользователь уже существует!!!")
                print('{', 'login:', ptr.login, ',', 'password:', ptr.password, '}\n')
            else:
                ptr = ptr.next
        else:
            print("Нет такого пользователя!\n")
        self.display_users()
        print("\n")

    def check_user_for_other_func(self, name):
        ptr = self.head
        while ptr is not None:
            if name == ptr.login:
                print("Такой пользователь уже существует!!!")
                print('{', 'login:', ptr.login, ',', 'password:', ptr.password, '}\n')
                return True
            else:
                ptr = ptr.next
        else:
            print("Нет такого пользователя!\n")
            return False

    def change_login(self):
        name = input("Укажите пользователя, у которого нужно заменить логин: ")
        if not UserList.verify_login(name):
            return False
        if self.check_user_for_other_func(name):
            ptr = self.head
            while ptr is not None:
                if ptr.login == name:
                    while True:
                        new_login = input("Введите новый логин: ")
                        if not UserList.verify_login(new_login):
                            return False
                        repeat_login = input("Введите новый логин еще раз: ")
                        if not UserList.verify_login(repeat_login):
                            return False
                        if new_login == repeat_login:
                            ptr.login = new_login
                            print("Логин изменен!")
                            self.display_users()
                            print("\n")
                            return ptr.login
                ptr = ptr.next

    def change_password(self):
        name = input("Укажите пользователя, у которого нужно заменить пароль: ")
        if not UserList.verify_login(name):
            return False
        if self.check_user_for_other_func(name):
            ptr = self.head
            while ptr is not None:
                if ptr.login == name:
                    while True:
                        new_password = input("Введите новый пароль: ")
                        if not UserList.verify_password(new_password):
                            return False
                        repeat_password = input("Введите новый пароль еще раз: ")
                        if not UserList.verify_password(repeat_password):
                            return False
                        if new_password == repeat_password:
                            ptr.password = new_password
                            print("Пароль изменен!")
                            self.display_users()
                            print("\n")
                            return ptr.password
                ptr = ptr.next

    def display_users(self):
        dictionary = {}
        count = 0
        ptr = self.head
        while ptr is not None:
            '''if ptr == self.head:
                print('         |', ptr.login, '|' + '\n' + 'None <--', '-'*(count + 4), '-->', end="")
            else:
                print('|', ptr.login, '|' + '\n' + ' <--', '-' * (count + 4), '-->', end="")'''
            key = ptr.login
            dictionary[key] = ptr.password
            #print(ptr, ptr.__dict__)
            ptr = ptr.next
        print("None <--> ", end="")
        for key, value in dictionary.items():
            count += 1
            print('[' + str(count) + ']', '{', 'login:', key, ',', 'password:', value, '}', '<--> ', end="")
        print(" None")

    @staticmethod
    def verify_login(value):
        pattern = r'\s'
        pattern2 = r'[0-9]'
        pattern3 = r'[а-яА-Я]'
        verify = re.search(pattern, value)
        verify2 = re.match(pattern2, value)
        verify3 = re.search(pattern3, value)

        if verify:
            print("Логин не должен содержать пробелы\n")
            return False

        if verify2:
            print("Логин не должен начинаться с цифры\n")
            return False
        if value == '':
            print("Нельзя ввести пустой логин\n")
            return False

        if verify3:
            print("Логин не должен содержать кириллицу\n")
            return False

        return True

    @staticmethod
    def verify_password(value):
        pattern = r'\s'
        pattern3 = r'[а-яА-Я]'
        verify = re.search(pattern, value)
        verify3 = re.search(pattern3, value)

        if verify:
            print("Пароль не должен содержать пробелы\n")
            return False

        if value == '':
            print("Нельзя ввести пустой пароль\n")
            return False

        if verify3:
            print("Пароль не должен содержать кириллицу\n")
            return False
        return True


user_list = UserList()

while True:
    menu = input("Выберите действие: \n"
                 "1-Добавить нового пользователя \n"
                 "2-Удалить существующего пользователя \n"
                 "3-Проверить существет ли пользователь \n"
                 "4-Изменить логин существующего пользователя \n"
                 "5-Изменить пароль существующего пользователя \n"
                 "6-выход из меню \n-> ")

    match menu:
        case "1":
            user_list.add_user()
        #
        case "2":
            user_list.delete_user()
        #
        case "3":
            user_list.check_user()

        case "4":
            user_list.change_login()

        case "5":
            user_list.change_password()

        case "6":
            break

        case _:
            print("Фиг тебе!")
