class Fraction:
    counter = 0

    def __init__(self, numerator=1, denominator=1):
        self.numerator = numerator
        self.denominator = denominator
        Fraction.counter += 1

    def division(self):
        return self.numerator / self.denominator

    @staticmethod
    def object_counting(count):
        return count


fraction = Fraction(3, 5)
fraction2 = Fraction(10, 20)
fraction3 = Fraction(10, 20)
fraction4 = Fraction(10, 20)
fraction5 = Fraction(10, 20)

print("Результат деления: ", fraction.division())
print("Результат деления: ", fraction2.division())

print("Количество созданных объектов: ", Fraction.object_counting(Fraction.counter))
