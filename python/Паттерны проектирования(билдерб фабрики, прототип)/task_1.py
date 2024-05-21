'''Используется Строитель'''


class KitchenAppliances:
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


class Builder:
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


class Director:
    """ Устанавливает либо базовые характеристики, либо уникальные"""
    def __init__(self):
        self.characteristics = Builder()

    def set_base_characteristics(self):
        self.characteristics.set_name()
        self.characteristics.set_color()
        self.characteristics.set_weight()
        self.characteristics.set_price()
        self.characteristics.set_power()
        return self.characteristics.get_device()

    def set_unique_characteristics(self):
        self.characteristics.set_tank_volume()
        self.characteristics.set_container_capacity()
        self.characteristics.set_pump_pressure()
        self.characteristics.set_bowl_volume()
        self.characteristics.set_number_of_speeds()
        self.characteristics.set_continuous_operation_time()
        self.characteristics.set_performance()
        return self.characteristics.get_device()

    def output_base_characteristics(self):
        print('\n')
        self.output_name()
        self.output_color()
        self.output_weight()
        self.output_price()
        self.output_power()

    def output_unique_characteristics(self):
        self.output_tank_volume()
        self.output_container_capacity()
        self.output_pump_pressure()
        self.output_bowl_volume()
        self.output_continuous_operation_time()
        self.output_number_of_speeds()
        self.output_performance()

    def output_name(self):
        print('Название: ' + self.characteristics.device.name)

    def output_color(self):
        print('Цвет: ' + self.characteristics.device.color)

    def output_weight(self):
        print('Масса: ' + self.characteristics.device.weight)

    def output_price(self):
        print('Цена: ' + self.characteristics.device.price)

    def output_power(self):
        print('Мощность: ' + self.characteristics.device.power)

    def output_tank_volume(self):
        print('Объем резервуара для воды: ' + self.characteristics.device.tank_volume)

    def output_container_capacity(self):
        print('Емкость контейнера: ' + self.characteristics.device.container_capacity)

    def output_pump_pressure(self):
        print('Давление помпы: ' + self.characteristics.device.pump_pressure)

    def output_bowl_volume(self):
        print('Объем чаши: ' + self.characteristics.device.bowl_volume)

    def output_continuous_operation_time(self):
        print('Количество скоростей: ' + self.characteristics.device.continuous_operation_time)

    def output_number_of_speeds(self):
        print('Время непрерывной работы: ' + self.characteristics.device.number_of_speeds)

    def output_performance(self):
        print('Производительность: ' + self.characteristics.device.performance)


builder = Builder()
director = Director()
print('Кофемашина\n')
coffee_machine = director.set_base_characteristics()
print('\n')
director.output_base_characteristics()
print('\n')
print('Соковыжималка\n')
juicer = director.set_unique_characteristics()
print('\n')
director.output_unique_characteristics()
print('\n')

print('Блендер\n')
blender = (builder.set_tank_volume()
           .set_price().set_pump_pressure()
           .set_number_of_speeds()
           .set_weight()
           .set_performance())
print('\n')
director.output_tank_volume()
director.output_price()
director.output_pump_pressure()
director.output_number_of_speeds()
director.output_weight()
director.output_performance()
print('\n')






