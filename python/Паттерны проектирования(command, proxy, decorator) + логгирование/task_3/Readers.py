from abc import ABC, abstractmethod
import re


class IReader(ABC):
    '''Интерфейс читателя'''
    @abstractmethod
    def about_reader(self): pass


class IBuilder(ABC):
    '''Интерфейс строителя'''
    @abstractmethod
    def set_login(self): pass

    @abstractmethod
    def set_id(self): pass

    @abstractmethod
    def set_age(self): pass

    @abstractmethod
    def set_subscription(self): pass

    @abstractmethod
    def set_address(self): pass


class IProxy(ABC):
    @abstractmethod
    def check_id_age(self, obj): pass

    @abstractmethod
    def check_login_address(self, obj): pass

    @abstractmethod
    def check_subscription(self, obj): pass


class Reader(IReader):
    def __init__(self):
        self.login = None
        self.id = None
        self.age = None
        self.subscription = None
        self.address = None
        self.books = []
        self.dict = {}

    def about_reader(self):
        print(end='\n')
        for key, value in self.dict.items():
            print(key, value)
        print(end='\n')


class Builder(IBuilder):
    def __init__(self):
        self.reader = Reader()

    def set_login(self):
        self.reader.login = input('Укажите логин читателя: ')
        self.reader.dict['Логин читателя:'] = self.reader.login
        return self

    def set_id(self):
        self.reader.id = input('Укажите id: ')
        self.reader.dict['id:'] = self.reader.id
        return self

    def set_age(self):
        self.reader.age = input('Укажите возраст: ')
        self.reader.dict['Возраст:'] = self.reader.age
        return self

    def set_subscription(self):
        self.reader.subscription = input('Абонимент: ')
        self.reader.dict['Абонимент:'] = self.reader.subscription
        return self

    def set_address(self):
        self.reader.address = input('Укажите адрес: ')
        self.reader.dict['Адрес:'] = self.reader.address
        return self

    def get_reader(self):
        return self.reader


class ProxyReader(IProxy):
    def check_id_age(self, obj):
        pattern = r'[^0-9]'
        if re.findall(pattern, obj.id):
            print(f'Поле id может содержать только цифры!')
            return False
        if re.findall(pattern, obj.age):
            print(f'Поле age может содержать только цифры!')
            return False
        return True

    def check_subscription(self, obj):
        pattern = r'yes|no'
        if not re.findall(pattern, obj.subscription.lower()):
            print(f'Поле subscription может содержать только yes или no!')
            return False
        return True

    def check_login_address(self, obj):
        pattern = r'\d|\s|[!@#№$%^&*()\-\_+=:;\"\'\\|\?/><.<`~,]'
        pattern2 = r'[!@#№$%^&*()\-\_+=:;\"\'\\|\?/><.<`~,]{2,}'
        if re.match(pattern, obj.login):
            print(f'Логин не может начинается с цифры, спецсимвола, пробельных знаков!')
            return False
        if re.search(pattern2, obj.login):
            print(f'В логине спецсимволы не могут следовать подряд!')
            return False
        if re.match(pattern, obj.address):
            print(f'Адрес не может начинается с цифры, спецсимвола, пробельных знаков!')
            return False
        if re.search(pattern2, obj.address):
            print(f'В адресе спецсимволы не могут следовать подряд!')
            return False
        return True

