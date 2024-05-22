from abc import ABC, abstractmethod
import re


class IBook(ABC):
    '''Интерфейс книги'''
    @abstractmethod
    def about_book(self): pass


class IBuilder(ABC):
    '''Интерфейс строителя'''
    @abstractmethod
    def set_name(self): pass

    @abstractmethod
    def set_publishing_house(self): pass

    @abstractmethod
    def set_number_of_pages(self): pass

    @abstractmethod
    def set_category(self): pass

    @abstractmethod
    def set_author(self): pass

    @abstractmethod
    def set_year(self): pass

    @abstractmethod
    def set_id(self): pass


class IProxy(ABC):
    @abstractmethod
    def check_id_year(self, obj): pass

    @abstractmethod
    def check_rest(self, obj): pass


class Book(IBook):
    '''Книга'''
    def __init__(self):
        self.name = None
        self.publishing_house = None
        self.year = None
        self.number_of_pages = None
        self.category = None
        self.author = None
        self.id = None
        self.dict = {}

    def about_book(self):
        print('\n')
        for key, value in self.dict.items():
            print(key, value)
        print(end='\n')


class Builder(IBuilder):
    def __init__(self):
        self.book = Book()

    def set_name(self):
        self.book.name = input('Укажите название книги: ')
        self.book.dict['Название книги:'] = self.book.name
        return self

    def set_publishing_house(self):
        self.book.publishing_house = input('Укажите издательство: ')
        self.book.dict['Издательство:'] = self.book.publishing_house
        return self

    def set_number_of_pages(self):
        self.book.number_of_pages = input('Укажите количество страниц: ')
        self.book.dict['Количество страниц:'] = self.book.number_of_pages
        return self

    def set_category(self):
        self.book.category = input('Укажите категорию: ')
        self.book.dict['Категория:'] = self.book.category
        return self

    def set_author(self):
        self.book.author = input('Укажите автора: ')
        self.book.dict['Автор:'] = self.book.author
        return self

    def set_year(self):
        self.book.year = input('Укажите год издания: ')
        self.book.dict['Год:'] = self.book.year
        return self

    def set_id(self):
        self.book.id = input('Укажите id книги: ')
        self.book.dict['id:'] = self.book.id
        return self

    def get_book(self):
        return self.book


class ProxyBook(IProxy):
    def check_id_year(self, obj):
        pattern = r'[^0-9]'
        if re.findall(pattern, obj.id):
            print(f'Поле id может содержать только цифры!')
            return False
        if re.findall(pattern, obj.year):
            print(f'Поле year может содержать только цифры!')
            return False
        if re.findall(pattern, obj.number_of_pages):
            print(f'Поле number_of_pages может содержать только цифры!')
            return False
        return True

    def check_rest(self, obj):
        pattern = r'\d|\s|[!@#№$%^&*()\-\_+=:;\"\'\\|\?/><.<`~,]'
        pattern2 = r'[!@#№$%^&*()\-\_+=:;\"\'\\|\?/><.<`~,]{2,}'
        if re.match(pattern, obj.name):
            print(f'Название не может начинается с цифры, спецсимвола, пробельных знаков!')
            return False
        if re.search(pattern2, obj.name):
            print(f'В названии спецсимволы не могут следовать подряд!')
            return False
        if re.match(pattern, obj.publishing_house):
            print(f'Издание не может начинается с цифры, спецсимвола, пробельных знаков!')
            return False
        if re.search(pattern2, obj.publishing_house):
            print(f'В издании спецсимволы не могут следовать подряд!')
            return False
        if re.match(pattern, obj.category):
            print(f'Категория не может начинается с цифры, спецсимвола, пробельных знаков!')
            return False
        if re.search(pattern2, obj.category):
            print(f'В категории спецсимволы не могут следовать подряд!')
            return False
        if re.match(pattern, obj.author):
            print(f'Автор не может начинается с цифры, спецсимвола, пробельных знаков!')
            return False
        if re.search(pattern2, obj.author):
            print(f'В авторе спецсимволы не могут следовать подряд!')
            return False
        return True


