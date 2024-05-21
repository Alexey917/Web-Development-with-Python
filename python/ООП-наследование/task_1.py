class Device:
    def __init__(self):
        self.name = ""
        self.color = ""
        self.weight = ""
        self.price = ""
        self.power = ""

    def set_property(self):
        self.name = input("Введите название -> ")
        self.color = input("Введите цвет -> ")
        self.weight = input("Введите массу -> ")
        self.price = input("Введите цену -> ")
        self.power = input("Введите мощность -> ")

    def get_property(self):
        print("\n---" + self.name + "---\n" +
              "цвет: " + self.color + "\n" +
              "вес: " + str(self.weight) + " кг" + "\n" +
              "мощность: " + str(self.power) + " Вт" + "\n" +
              "цена: " + str(self.price) + " руб.")


class CoffeMachine(Device):
    def __init__(self, tank_volume, container_capacity, pump_pressure):
        super().__init__()
        self.tank_volume = tank_volume
        self.container_capacity = container_capacity
        self.pump_pressure = pump_pressure

    def set_property(self):
        self.name = "Кофемашина автоматическая Philips EP1000/00"
        self.color = "черный"
        self.weight = 7.5
        self.price = 25000
        self.power = 1500

    def get_property(self):
        super().get_property()
        print("объем резервуара для воды: " + str(self.tank_volume) + " л" + "\n" +
              "давление помпы: " + str(self.pump_pressure) + " Бар" + "\n" +
              "емкость контейнера для зерен: " + str(self.container_capacity) + " г" + "\n")


class Blender(Device):
    def __init__(self):
        super().__init__()
        self.number_of_speeds = ""
        self.bowl_volume = ""
        self.power_settings = ""

    def set_property(self):
        super().set_property()
        self.number_of_speeds = input("Введите количество скоростей -> ")
        self.bowl_volume = input("Введите объем чаши -> ")
        self.power_settings = input("Введите параметры мощности -> ")

    def get_property(self):
        super().get_property()
        print("количество скоростей: " + self.number_of_speeds + "\n" +
              "объем чаши: " + self.bowl_volume + " л" + "\n" +
              "параметры мощности: " + self.power_settings + " В/Гц" + "\n")


class MeatGrinder(Device):
    def __init__(self, continuous_operation_time, performance, tray_material):
        super().__init__()
        self.continuous_operation_time = continuous_operation_time
        self.performance = performance
        self.tray_material = tray_material

    def get_property(self):
        super().get_property()
        print("время непрерывной работы: " + self.continuous_operation_time + " мин" + "\n" +
              "производительность: " + self.performance + " кг/мин" + "\n" +
              "материал лотка: " + self.tray_material + "\n")


device = Device()
device.set_property()
device.get_property()

coffee = CoffeMachine("1.8", "275", "15")
coffee.set_property()
coffee.get_property()

blender = Blender()
blender.set_property()
blender.get_property()

meat = MeatGrinder("10", "0.58", "пластик")
meat.set_property()
meat.get_property()

