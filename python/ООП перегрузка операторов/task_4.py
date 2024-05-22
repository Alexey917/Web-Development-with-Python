class Flat:
    def __init__(self):
        self.price = None
        self.square = None

    def set_options(self):
        self.square = float(input('Задайте площадь квартиры: '))
        self.price = int(input('Задайте цену квартире: '))

    @classmethod
    def verify_data(cls, other):
        if not isinstance(other, Flat):
            raise TypeError("Операнд справа должен принадлежать классу Flat")
        return other

    def __eq__(self, other):
        other = self.verify_data(other)
        return self.square == other.square

    def __ne__(self, other):
        other = self.verify_data(other)
        return self.square != other.square

    def __gt__(self, other):
        other = self.verify_data(other)
        return self.price > other.price

    def __ge__(self, other):
        other = self.verify_data(other)
        return self.price >= other.price

    def __str__(self):
        return (f'Цена квартиры: {self.price}, '
                f'площадь квартиры: {self.square},')


flat1 = Flat()
flat1.set_options()
flat2 = Flat()
flat2.set_options()

print(flat1 == flat2)
print(flat1 != flat2)
print(flat1 <= flat2)

