class Complex:
    def __init__(self):
        self.a = None  # действительная часть
        self.b = None  # мнимая часть

    def set_options(self):
        self.a = int(input('Задайте действительную часть: '))
        self.b = int(input('Задайте мнимую часть: '))

    def __add__(self, other):
        complex_num = Complex()
        complex_num.a = self.a + other.a
        complex_num.b = self.b + other.b
        return complex_num

    def __sub__(self, other):
        complex_num = Complex()
        complex_num.a = self.a - other.a
        complex_num.b = self.b - other.b
        return complex_num

    def __mul__(self, other):
        complex_num = Complex()
        complex_num.a = (self.a * other.a) - (self.b * other.b)
        complex_num.b = (self.a * other.b) + (self.b * other.a)
        return complex_num

    def __truediv__(self, other):
        complex_num = Complex()
        complex_num.a = ((self.a * other.a) + (self.b * other.b)) / ((pow(other.a, 2)) + (pow(other.b, 2)))

        complex_num.b = ((other.a * self.b) - (self.a * other.b)) / ((pow(other.a, 2)) + (pow(other.b, 2)))
        return complex_num

    def __str__(self):
        return f'z = {self.a} + {self.b}i'


c_num1 = Complex()
c_num2 = Complex()
c_num1.set_options()
c_num2.set_options()

print('Результат сложения', c_num_sum := c_num1 + c_num2)
print('Результат вычитания', c_num_minus := c_num1 - c_num2)
print('Результат умножения', c_num_mul := c_num1 * c_num2)
print('Результат деления', c_num_div := c_num1 / c_num2)
