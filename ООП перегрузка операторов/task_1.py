class Circle:
    def __init__(self):
        self.r = None
        self.c = None  # длина окружности

    def set_options(self):
        self.r = int(input('Задайте радиус окружности: '))
        self.c = int(input('Задайте длину окружности: '))

    @classmethod
    def verify_data(cls, other):
        if not isinstance(other, Circle):
            raise TypeError("Операнд справа должен принадлежать классу Circle")
        return other

    @classmethod
    def verify_change(cls, other):
        if not isinstance(other, (int, float)):
            raise TypeError("Операнд справа должен быть числом")
        return other

    def __eq__(self, other):
        other = self.verify_data(other)
        return self.r == other.r

    def __lt__(self, other):
        other = self.verify_data(other)
        return self.c < other.c

    def __le__(self, other):
        other = self.verify_data(other)
        return self.c <= other.c

    def __iadd__(self, other):
        other = self.verify_change(other)
        self.r += other
        self.c += other
        return self

    def __add__(self, other):
        circle = Circle()
        circle.r = self.r + other.r
        circle.c = self.c + other.c
        return circle

    def __isub__(self, other):
        other = self.verify_change(other)
        self.r -= other
        self.c -= other
        return self

    def __sub__(self, other):
        circle = Circle()
        circle.r = self.r - other.r
        circle.c = self.c - other.c
        return circle

    def __str__(self):
        return f'Радиус окружности: {self.r}, длина окружности: {self.c} '


circle1 = Circle()
circle1.set_options()
circle2 = Circle()
circle2.set_options()

print(circle1 == circle2)
print(circle1 <= circle2)
print(circle1 > circle2)
circle1 += 10.5
print(f'Длина окружности при увеличении радиуса: {circle1}')
circle2 -= 4.7
print(f'Длина окружности при уменьшении радиуса: {circle2}')
# circle2
circle2 = circle1 + circle2
print(f'размеры окружности: {circle2}')
circle3 = circle2 - circle1
print(f'размеры окружности: {circle3}')

