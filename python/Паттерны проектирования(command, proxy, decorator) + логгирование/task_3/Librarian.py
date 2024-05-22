'''Запускать программу от сюда ;)'''
import Readers
import Books
from collections.abc import Iterable, Iterator
from abc import ABC, abstractmethod
import pickle
import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler(f"{__name__}.log", mode='w')
formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

class ILibrarian(ABC):
    @abstractmethod
    def switch_builder(self): pass


class Librarian(ILibrarian):
    def __init__(self):
        self.data = None
        self.book_base = []
        self.reader_base = []

    def add_item(self):
        '''Добавляет пользователя в базу данных'''
        print(f'Добавьте пользователя/книгу в базу данных:\n')
        logger.info(f'Добавьте пользователя/книгу в базу данных')
        self.data = self.switch_builder()
        if isinstance(self.data, Books.Book):
            proxy_book = Books.ProxyBook()
            if not proxy_book.check_id_year(self.data):
                return False
            if not proxy_book.check_rest(self.data):
                return False
            self.book_base.append(self.data)
        else:
            proxy_reader = Readers.ProxyReader()
            if not proxy_reader.check_id_age(self.data):
                return False
            if not proxy_reader.check_subscription(self.data):
                return False
            if not proxy_reader.check_login_address(self.data):
                return False
            self.reader_base.append(self.data)
        print(end='\n')
        print(f'Пользователь/книга добавлен(а)!\n')
        logger.info(f'Пользователь/книга добавлен(а)!')

    def delete_item(self):
        '''Удаляет пользователя из базы данных'''
        id_obj = Librarian.input_id()
        if type(self.data) is Books.Book:
            r = LibrarianAggregate(self.book_base)
            for item in r:
                if item.id == str(id_obj):
                    self.book_base.remove(item)
        else:
            r = LibrarianAggregate(self.reader_base)
            for item in r:
                if item.id == str(id_obj):
                    self.reader_base.remove(item)
        print(f'Пользователь/книга удален(а)!', end='\n')
        logger.info(f'Пользователь/книга удален(а)!')

    def change_item(self):
        '''Изменяем данные о пользователе'''
        id_obj = Librarian.input_id()
        if type(self.data) is Books.Book:
            r = LibrarianAggregate(self.book_base)
            count = 0
            for item in r:
                if item.id == str(id_obj):
                    count += 1
                    print(end='\n')
                    logger.info(f'Что именно хотите изменить?')
                    key = input(f'Что именно хотите изменить?\n'
                                f'1-Название книги\n'
                                f'2-Издательство\n'
                                f'3-Количество страниц\n'
                                f'4-Категория\n'
                                f'5-Автор\n'
                                f'6-Год\n'
                                f'7-id\n->')
                    while True:
                        match key:
                            case "1":
                                logger.info(f'Меняем название книги')
                                item.dict['Название книги:'] = input('Новое значение ->')
                                print(f'Значение изменено!\n')
                                logger.info(f'Значение изменено!')
                                break
                            case "2":
                                logger.info(f'Меняем издательство')
                                item.dict['Издательство:'] = input('Новое значение ->')
                                print(f'Значение изменено!\n')
                                logger.info(f'Значение изменено!')
                                break
                            case "3":
                                logger.info(f'Меняем количество страниц')
                                item.dict['Количество страниц:'] = input('Новое значение ->')
                                print(f'Значение изменено!\n')
                                logger.info(f'Значение изменено!')
                                break
                            case "4":
                                logger.info(f'Меняем категорию')
                                item.dict['Категория:'] = input('Новое значение ->')
                                print(f'Значение изменено!\n')
                                logger.info(f'Значение изменено!')
                                break
                            case "5":
                                logger.info(f'Меняем автора')
                                item.dict['Автор:'] = input('Новое значение ->')
                                print(f'Значение изменено!\n')
                                logger.info(f'Значение изменено!')
                                break
                            case "6":
                                logger.info(f'Меняем год')
                                item.dict['Год:'] = input('Новое значение ->')
                                print(f'Значение изменено!\n')
                                logger.info(f'Значение изменено!')
                                break
                            case "7":
                                logger.info(f'Меняем id')
                                item.dict['id:'] = input('Новое значение ->')
                                print(f'Значение изменено!\n')
                                logger.info(f'Значение изменено!')
                                break
                            case _:
                                print(f'Такого ключа не существует! Попробуйте еще раз\n')
                                logger.warning(f'Такого ключа не существует! Попробуйте еще раз')
                                break
            if count == 0:
                print(f'Книги с таким id не существует!\n')
                logger.warning(f'Книги с таким id не существует!')
        else:
            r = LibrarianAggregate(self.reader_base)
            count = 0
            for item in r:
                if item.id == str(id_obj):
                    count += 1
                    print(end='\n')
                    logger.info(f'Что именно хотите изменить?')
                    key = input(f'Что именно хотите изменить?\n'
                                f'1-Логин\n'
                                f'2-id\n'
                                f'3-Возраст\n'
                                f'4-Абонимент\n'
                                f'5-Адрес\n->')
                    while True:
                        match key:
                            case "1":
                                logger.info(f'Меняем логин читателя')
                                item.dict['Логин читателя:'] = input('Новое значение ->')
                                print(f'Значение изменено!\n')
                                logger.info(f'Значение изменено!')
                                break
                            case "2":
                                logger.info(f'Меняем id')
                                item.dict['id:'] = input('Новое значение ->')
                                print(f'Значение изменено!\n')
                                logger.info(f'Значение изменено!')
                                break
                            case "3":
                                logger.info(f'Меняем возраст')
                                item.dict['Возраст:'] = input('Новое значение ->')
                                print(f'Значение изменено!\n')
                                logger.info(f'Значение изменено!')
                                break
                            case "4":
                                logger.info(f'Меняем абонимент')
                                item.dict['Абонимент:'] = input('Новое значение ->')
                                print(f'Значение изменено!\n')
                                logger.info(f'Значение изменено!')
                                break
                            case "5":
                                logger.info(f'Меняем адрес')
                                item.dict['Адрес:'] = input('Новое значение ->')
                                print(f'Значение изменено!\n')
                                logger.info(f'Значение изменено!')
                                break
                            case _:
                                print(f'Такого ключа не существует! Попробуйте еще раз\n')
                                logger.warning(f'Такого ключа не существует! Попробуйте еще раз')
                                break
            if count == 0:
                print(f'Пользователя с таким id не существует!\n')
                logger.warning(f'Пользователя с таким id не существует!')

    def save_in_file(self):
        ''''Сохраняет данные в файл'''
        with open('readers.bin', 'wb') as f:
            if type(self.data) is Books.Book:
                r = LibrarianAggregate(self.book_base)
                li = []
                for item in r:
                    li.append(item)
                pickle.dump(li, f)
            else:
                r = LibrarianAggregate(self.reader_base)
                li = []
                for item in r:
                    li.append(item)
                pickle.dump(li, f)

    def load_in_file(self):
        ''''Загружает данные из файла'''
        with open('readers.bin', 'rb') as f:
            if type(self.data) is Books.Book:
                data = pickle.load(f)
                for item in data:
                    item.about_book()
            else:
                data = pickle.load(f)
                for item in data:
                    item.about_reader()

    def search_item(self):
        id_obj = Librarian.input_id()
        if type(self.data) is Books.Book:
            r = LibrarianAggregate(self.book_base)
            count = 0
            for item in r:
                if item.id == str(id_obj):
                    count += 1
                    item.about_book()
            if count == 0:
                print(f'Пользователя с таким id не существует!\n')
                logger.warning(f'Пользователя с таким id не существует!')
        else:
            r = LibrarianAggregate(self.reader_base)
            count = 0
            for item in r:
                if item.id == str(id_obj):
                    count += 1
                    item.about_reader()
            if count == 0:
                print(f'Книги с таким id не существует!\n')
                logger.warning(f'Книги с таким id не существует!')

    def show_database(self):
        print(f'Список данных:', end='\n')
        if type(self.data) is Books.Book:
            r = LibrarianAggregate(self.book_base)
            for item in r:
                item.about_book()
        else:
            r = LibrarianAggregate(self.reader_base)
            for item in r:
                item.about_reader()

    def switch_builder(self):
        while True:
            logger.info(f'Выберите раздел с которым будем работать')
            item = input("Выберите раздел с которым будем работать: \n"
                         "1-Книги\n"
                         "2-Читатели\n ->")

            match item:
                case "1":
                    logger.info(f'Выбран раздел книги')
                    builder = Books.Builder()
                    book = (builder.set_name()
                            .set_publishing_house()
                            .set_number_of_pages()
                            .set_category()
                            .set_author()
                            .set_year()
                            .set_id()
                            .get_book())
                    return book

                case "2":
                    logger.info(f'Выбран раздел читатели')
                    builder = Readers.Builder()
                    reader = (builder.set_login().set_id().set_age().set_address().set_subscription().get_reader())
                    return reader
                case _:
                    print(f'Нет такого пункта меню!')
                    logger.warning(f'Нет такого пункта меню!')

    def switch_chapter(self):
        while True:
            item = input("Выберите раздел с которым будем работать: \n"
                         "1-Книги\n"
                         "2-Читатели\n ->")

            match item:
                case "1":
                    logger.info(f'Выбран раздел книги')
                    self.data = Books.Book()
                    break
                case "2":
                    logger.info(f'Выбран раздел читатели')
                    self.data = Readers.Reader()
                    break
                case _:
                    print(f'Нет такого пункта меню!')
                    logger.warning(f'Нет такого пункта меню!')

    @staticmethod
    def input_id():
        try:
            logger.info(f'Указываем id для поиска')
            id_inp = int(input(f'укажите id: '))
            return id_inp
        except ValueError:
            print(f'Указан не верный тип значения!')
            logger.error(f'Указан не верный тип значения!', exc_info=True)


class LibrarianIterator(Iterator):
    '''Реализуем итератор'''
    # принимает список читателей
    def __init__(self, readers,
                 reverse: bool = False):
        self.reader = readers
        self.index: int = -1 if reverse else 0
        self.reverse = reverse

    def __next__(self):
        try:
            # сохраняет текущего читателя
            user = self.reader[self.index]
            # увеличивает индекс на 1
            self.index += -1 if self.reverse else 1
        except IndexError:
            raise StopIteration()
        # возвращает текущего читателя
        return user


class LibrarianAggregate(Iterable):
    def __init__(self, data: list):
        self.data = data

    def __iter__(self) -> LibrarianIterator:
        return LibrarianIterator(self.data)

    def get_reverse_iterator(self) -> LibrarianIterator:
        return LibrarianIterator(self.data, True)


class IProxyLogging(ABC):
    @abstractmethod
    def set_logs(self): pass

    @abstractmethod
    def log_info(self, string): pass

    @abstractmethod
    def log_warning(self, string): pass

    @abstractmethod
    def log_error(self, string): pass


# class ProxyLogging(IProxyLogging):
#     # def __init__(self):
#     #     self.logger = None
#     #     self.handler = None
#     #     self.formatter = None
#
#     def set_logs(self):
#         logger = logging.getLogger(__name__)
#         logger.setLevel(logging.INFO)
#         handler = logging.FileHandler(f"{__name__}.log", mode='w')
#         formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
#         handler.setFormatter(formatter)
#         logger.addHandler(handler)
#         return logger
#
#     def log_info(self, string):
#         self.set_logs().info(string)
#
#     def log_warning(self, string):
#         self.set_logs().warning(string)
#
#     def log_error(self, string):
#         self.set_logs().error(string, exc_info=True)


librarian = Librarian()
#proxy_log = ProxyLogging()
#proxy_log.set_logs()


def get_menu():
    while True:
        menu = input("Выберите действие: \n"
                     "----------------------------------------\n"
                     "1-Добавить данные о (книге/читателе)\n"
                     "2-Удалить данные о (книге/читателе)\n"
                     "3-Изменить данные о (книге/читателе)\n"
                     "4-Поиск данных о (книге/читателе)\n"
                     "5-Отобразить данные о  (книге/читателе)\n"
                     "6-Сохранить данные в файл\n"
                     "7-Загрузить данные из файла\n"
                     "8-Смена раздела\n"
                     "9-Выход из меню\n"
                     "----------------------------------------"
                     "\n-> ")

        match menu:
            case "1":
                logger.info(f'Добавляем пользователя/книгу')
                librarian.add_item()
            case "2":
                logger.info(f'Удаляем пользователя/книгу')
                librarian.delete_item()
            case "3":
                logger.info(f'Изменяем данные о пользователе/книге')
                librarian.change_item()
            case "4":
                logger.info(f'Ищем о пользователя/книгу')
                librarian.search_item()
            case "5":
                logger.info(f'Отображаем данные о пользователе/книге')
                librarian.show_database()
            case "6":
                logger.info(f'Сохраняем данные в файл')
                librarian.save_in_file()
            case "7":
                logger.info(f'Загружаем данные из файл')
                librarian.load_in_file()
            case "8":
                logger.info(f'Меняем раздел')
                librarian.switch_chapter()
            case "9":
                logger.info(f'Выход из меню')
                break
            case _:
                print(f'Нет такого пункта меню!')
                logger.warning(f'Нет такого пункта меню!')


get_menu()

