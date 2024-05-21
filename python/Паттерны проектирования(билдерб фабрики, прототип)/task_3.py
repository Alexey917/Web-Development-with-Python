'''Используется Прототип'''

from abc import ABC, abstractmethod
import copy


class IProtype(ABC):
    @abstractmethod
    def clone(self): pass


class KitchenAppliances():
    """ Техника для кухни """

    def __init__(self):
        self.name = ""
        self.color = ""
        self.weight = ""
        self.price = ""
        self.power = ""
        self.tank_volume = ""
        self.container_capacity = ""
        self.pump_pressure = ""
        self.bowl_volume = ""
        self.number_of_speeds = ""
        self.continuous_operation_time = ""
        self.performance = ""



class Builder(IProtype):
    """ Использую строитель для отделения конструирования объекта от его представления """

    def __init__(self):
        self.device = KitchenAppliances()

    def set_name(self):
        self.device.name = input("Введите название -> ")
        return self

    def set_color(self):
        self.device.color = input("Введите цвет -> ")
        return self

    def set_weight(self):
        self.device.weight = input("Введите массу -> ")
        return self

    def set_price(self):
        self.device.price = input("Введите цену -> ")
        return self

    def set_power(self):
        self.device.power = input("Введите мощность -> ")
        return self

    def set_tank_volume(self):
        self.device.tank_volume = input("Введите объем резервуара для воды -> ")
        return self

    def set_container_capacity(self):
        self.device.container_capacity = input("Введите емкость контейнера -> ")
        return self

    def set_pump_pressure(self):
        self.device.pump_pressure = input("Введите давление помпы -> ")
        return self

    def set_bowl_volume(self):
        self.device.bowl_volume = input("Введите объем чаши -> ")
        return self

    def set_number_of_speeds(self):
        self.device.number_of_speeds = input("Введите количество скоростей -> ")
        return self

    def set_continuous_operation_time(self):
        self.device.continuous_operation_time = input("Введите время непрерывной работы -> ")
        return self

    def set_performance(self):
        self.device.performance = input("Введите производительность -> ")
        return self

    def get_device(self):
        return self.device

    def clone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return (f'Название: {self.device.name}\n'
                f'Цвет: {self.device.color}\n'
                f'Масса: {self.device.weight}\n'
                f'Цена: {self.device.price}\n'
                f'Мощность: {self.device.power}\n'
                f'Объем резервуара для воды: {self.device.tank_volume}\n'
                f'Емкость контейнера: {self.device.container_capacity}\n'
                f'Давление помпы: {self.device.pump_pressure}\n'
                f'Объем чаши: {self.device.bowl_volume}\n'
                f'Количество скоростей: {self.device.continuous_operation_time}\n'
                f'Время непрерывной работы: {self.device.number_of_speeds}\n'
                f'Производительность: {self.device.performance}\n')


builder = Builder()

print('Кофемашина\n')
coffee_machine = builder.set_name().set_color().set_number_of_speeds().set_performance().set_price()
print('\n')
print(coffee_machine)

new_coffee_machine = coffee_machine.clone()
print(new_coffee_machine)
new_coffee_machine.set_name().set_color()
print(coffee_machine)
print(new_coffee_machine)

