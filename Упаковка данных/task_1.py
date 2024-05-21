import pickle
import json
from datetime import datetime


class Car:
    def __init__(self, model, year, manufacturer, capacity, color, price):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.capacity = capacity
        self.color = color
        self.price = price

    def __str__(self):
        return (f"Модель: {self.model}\n"
                f"Год выпуска: {self.year}\n"
                f"Производитель: {self.manufacturer}\n"
                f"Объем двигателя: {self.capacity}\n"
                f"Цвет: {self.color}\n"
                f"Цена: {self.price}\n")

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

    @staticmethod
    def serialization_bin(obj):
        with open('my_file.bin', 'wb') as file:
            pickle.dump(obj, file)

    @staticmethod
    def deserialization_bin():
        with open('my_file.bin', 'rb') as file:
            data = pickle.load(file)
            print(data, '\n')

    def serialization_json(self):
        with open('my_file.json', 'w') as file:
            json.dump([self.model, self.year, self.manufacturer, self.capacity, self.color, self.price], file)

    @staticmethod
    def deserialization_json():
        with open('my_file.json', 'r') as file:
            data = json.load(file)
            print(data, '\n')


car = Car("Toyota GR Yaris IV", 2020, "Gazoo Racing", "1618 см³", "white", 8280000)
print(car)
print(car.out_model())
print(car.out_year())
print(car.out_manufacturer())
print(car.out_capacity())
print(car.out_color())
print(car.out_price(), '\n')

start_time = datetime.now()
Car.serialization_bin(car)
Car.deserialization_bin()
end_time = datetime.now()
execution_time = end_time - start_time

start_time2 = datetime.now()
Car.serialization_json(car)
Car.deserialization_json()
end_time2 = datetime.now()
execution_time2 = end_time2 - start_time2

print('Время работы с использованием pickle:', execution_time)
print('Время работы с использованием json:', execution_time)
