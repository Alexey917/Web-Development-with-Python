import pickle
import json
from datetime import datetime


class Book:
    def __init__(self):
        self.name_book = ""
        self.year = ""
        self.publisher = ""
        self.genre = ""
        self.author = ""
        self.price = ""

    def input_book(self):
        self.name_book = input("Введите название книги: ")
        self.year = input("Введите год выпуска: ")
        self.publisher = input("Введите издателя: ")
        self.genre = input("Введите жанр: ")
        self.author = input("Введите автора: ")
        self.price = input("Введите цену: ")

    def output_book(self):
        print(
            f'\nНазвание -> {self.name_book}\n'
            f'Год выпуска -> {self.year}\n'
            f'Издатель -> {self.publisher}\n'
            f'Жанр -> {self.genre}\n'
            f'Автор -> {self.author}\n'
            f'Цена -> {self.price}'
        )

    def output_name(self):
        return f'\nНазвание -> {self.name_book}'

    def output_year(self):
        return f'Год выпуска -> {self.year}'

    def output_publisher(self):
        return f'Издатель -> {self.publisher}'

    def output_genre(self):
        return f'Жанр -> {self.genre}'

    def output_author(self):
        return f'Автор -> {self.author}'

    def output_price(self):
        return f'Цена -> {self.price}'

    def __str__(self):
        return (f"Название: {self.name_book}\n"
                f"Год выпуска: {self.year}\n"
                f"Издатель: {self.publisher}\n"
                f"Жанр: {self.genre}\n"
                f"Автор: {self.author}\n"
                f"Цена: {self.price}\n")

    @staticmethod
    def serialization_bin(obj):
        with open('for_task_2.bin', 'wb') as file:
            pickle.dump(obj, file)

    @staticmethod
    def deserialization_bin():
        with open('for_task_2.bin', 'rb') as file:
            data = pickle.load(file)
            print(data, '\n')

    def serialization_json(self):
        with open('for_task_2.json', 'w') as file:
            json.dump([self.output_name(), self.output_year(), self.output_publisher(), self.output_genre(), self.output_author(), self.output_price()], file)

    @staticmethod
    def deserialization_json():
        with open('for_task_2.json', 'r') as file:
            data = json.load(file)
            print(data, '\n')


book = Book()
book.input_book()
book.output_book()
print(book.output_name())
print(book.output_year())
print(book.output_publisher())
print(book.output_genre())
print(book.output_author())
print(book.output_price(), '\n')

start_time = datetime.now()
Book.serialization_bin(book)
Book.deserialization_bin()
end_time = datetime.now()
execution_time = end_time - start_time

start_time2 = datetime.now()
Book.serialization_json(book)
Book.deserialization_json()
end_time2 = datetime.now()
execution_time2 = end_time2 - start_time2

print('Время работы с использованием pickle:', execution_time)
print('Время работы с использованием json:', execution_time)
