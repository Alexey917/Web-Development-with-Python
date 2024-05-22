class Date:
    YEAR = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self):
        self.day = None
        self.month = None
        self.year = None
        self.convert = 0

    def set_date(self):
        self.day = int(input('Введите день: '))
        self.month = int(input('Введите месяц: '))
        self.year = int(input('Введите год: '))

    def verify_date(self):
        limit = Date.YEAR[self.month - 1]
        if self.day > limit:
            raise ValueError('В этом месяце нет такого количества дней!')
        if self.month > 12:
            raise ValueError('Не бывает больше 12 месяцев!')
        if self.day < 0 or self.month < 0 or self.year < 0:
            raise ValueError('Дата не имеет отрицательных значений!')
        return True

    def converting(self):
        for month in range(self.month - 1):
            self.convert += Date.YEAR[month]
        self.convert += (self.year * 365) + self.day
        return self.convert

    def __str__(self):
        return f'{self.day}.{self.month}.{self.year}'

    def __sub__(self, other):
        date = Date()
        date.convert = self.convert - other.convert
        return date


date1 = Date()
date2 = Date()

while True:
    date1.set_date()
    date2.set_date()
    if date1.verify_date() and date2.verify_date():
        break

print(date1)
print(date1.converting())
print(date2)
print(date2.converting())

#print(res_date := date1 - date2)
