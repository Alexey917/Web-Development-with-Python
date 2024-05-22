class Airplane:
    def __init__(self):
        self.num_of_pas = None   # количество пассажиров в салоне
        self.max_num_of_pas = None   # максимальное количество пассажиров на борту
        self.type = None  # тип самолета

    def set_options(self):
        self.num_of_pas = int(input('Задайте количество пассажиров в салоне: '))
        self.max_num_of_pas = int(input('Задайте максимальное количество пассажиров на борту: '))
        self.type = input('Задайте тип самолета: ')

    @classmethod
    def verify_data(cls, other):
        if not isinstance(other, Airplane):
            raise TypeError("Операнд справа должен принадлежать классу Airplane")
        return other

    @classmethod
    def verify_change(cls, other):
        if not isinstance(other, int):
            raise TypeError("Операнд справа должен быть числом")
        return other

    def __eq__(self, other):
        other = self.verify_data(other)
        return self.type.lower() == other.type.lower()

    def __lt__(self, other):
        other = self.verify_data(other)
        return self.max_num_of_pas < other.max_num_of_pas

    def __le__(self, other):
        other = self.verify_data(other)
        return self.max_num_of_pas <= other.max_num_of_pas

    def __iadd__(self, other):
        other = self.verify_change(other)
        self.num_of_pas += other
        return self

    def __add__(self, other):
        airplane = Airplane()
        airplane.num_of_pas = self.num_of_pas + other.num_of_pas
        return airplane

    def __isub__(self, other):
        other = self.verify_change(other)
        self.num_of_pas -= other
        return self

    def __sub__(self, other):
        airplane = Airplane()
        airplane.num_of_pas = self.num_of_pas - other.num_of_pas
        return airplane

    def __str__(self):
        return (f'Тип самолета: {self.type}, '
                f'количество пассажиров в салоне: {self.num_of_pas},'
                f'максимальное количество пассажиров на борту: {self.max_num_of_pas}')


airplane1 = Airplane()
airplane1.set_options()
airplane2 = Airplane()
airplane2.set_options()

print(airplane1 == airplane2)
print(airplane1 >= airplane2)
print(airplane1 < airplane2)
airplane1 += 12
print(f'Количество пассажиров в первом салоне: {airplane1.num_of_pas}')
airplane2 -= 8
print(f'Количество пассажиров во втором салоне: {airplane2.num_of_pas}')
# # circle2
airplane2 = airplane1 + airplane2
print(f'Количество пассажиров во втором салоне: {airplane2.num_of_pas}')
airplane3 = airplane2 - airplane1
print(f'Количество пассажиров во втором салоне: {airplane3.num_of_pas}')