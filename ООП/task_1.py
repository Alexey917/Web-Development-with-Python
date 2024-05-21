class Car:
    def __init__(self, model, year, manufacturer, capacity, color, price):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.capacity = capacity
        self.color = color
        self.price = price

    def __str__(self):
        return f"Модель: {self.model}\nГод выпуска: {self.year}\nПроизводитель: {self.manufacturer}\nОбъем двигателя: {self.capacity}\nЦвет: {self.color}\nЦена: {self.price}\n"

    def out_model(self):
        return self.model

    def out_year(self):
        return self.year

    def out_manufacturer(self):
        return self.manufacturer

    def out_capacity(self):
        return self.capacity

    def out_color(self):
        return self.color

    def out_price(self):
        return self.price


car = Car("Toyota GR Yaris IV", 2020, "Gazoo Racing", "1618 см³", "white", 8280000)
print(car)
print(car.out_model())
print(car.out_year())
print(car.out_manufacturer())
print(car.out_capacity())
print(car.out_color())
print(car.out_price())
