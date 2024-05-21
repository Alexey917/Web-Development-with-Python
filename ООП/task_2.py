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


book = Book()
book.input_book()
book.output_book()
print(book.output_name())
print(book.output_year())
print(book.output_publisher())
print(book.output_genre())
print(book.output_author())
print(book.output_price())
