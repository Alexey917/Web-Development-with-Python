class Money:
    def __init__(self):
        self.rubbles = 0
        self.kopecks = 0
        self.total = 0.0

    def input(self):
        self.rubbles = int(input("Введите значение целой части: "))
        self.kopecks = int(input("Введите значение дробной части: "))

    def total_money(self):
        if self.kopecks > 100:
            self.rubbles = self.rubbles + (self.kopecks // 100)
            self.kopecks = self.kopecks % 100
        return self.rubbles, self.kopecks

    def __str__(self):
        return f"{self.rubbles} рублей {self.kopecks} копеек"

    def for_convert(self):
        self.total = f"{self.rubbles}.{self.kopecks}"
        self.total = float(self.total)
        return self.total

    def __add__(self, other):
        return self.total + other.total


class Dollars(Money):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return f"{self.rubbles} долларов {self.kopecks} центов"

    def convert(self):
        self.total = float(self.total) * 89.46
        return f'{round(self.total, 3)} рублей'


class Euros(Money):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return f"{self.rubbles} евро {self.kopecks} евроцентов"

    def convert(self):
        self.total = float(self.total) * 97.13
        return f'{round(self.total, 3)} рублей'


class Hryvnia(Money):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return f"{self.rubbles} гривен {self.kopecks} копеек"

    def convert(self):
        self.total = float(self.total) * 2.47
        return f'{round(self.total, 3)} рублей'


money = Money()
money.input()
money.total_money()
print(money)
print(money.for_convert())

dollar = Dollars()
dollar.input()
dollar.total_money()
print(dollar)
dollar.for_convert()
print(dollar.convert())

euro = Euros()
euro.input()
euro.total_money()
print(euro)
euro.for_convert()
print(euro.convert())

hryvnia = Hryvnia()
hryvnia.input()
hryvnia.total_money()
print(hryvnia)
hryvnia.for_convert()
print(hryvnia.convert())


res1 = hryvnia + dollar
res2 = money + euro
res3 = hryvnia + money
res4 = dollar + euro
print(round(res1, 2), "руб.", round(res2, 2), "руб.",  round(res3, 2), "руб.",  round(res4, 2), "руб.")


