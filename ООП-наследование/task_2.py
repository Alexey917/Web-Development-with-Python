class Ship:
    def __init__(self):
        self.name = ""
        self.color = ""
        self.weight = ""
        self.width = ""
        self.speed = ""

    def set_property(self):
        self.name = input("Введите название -> ")
        self.color = input("Введите цвет -> ")
        self.weight = input("Введите вес -> ")
        self.width = input("Введите ширину -> ")
        self.speed = input("Введите скорость -> ")

    def get_property(self):
        print("\n---" + self.name + "---\n" +
              "цвет: " + self.color + "\n" +
              "вес: " + str(self.weight) + " т" + "\n" +
              "ширина: " + str(self.width) + " м" + "\n" +
              "скорость: " + str(self.speed) + " км/ч.")


class Frigate(Ship):
    def __init__(self, number_of_decks, cruising_range, length):
        super().__init__()
        self.number_of_decks = number_of_decks
        self.cruising_range = cruising_range
        self.length = length

    def set_property(self):
        self.name = "Боевые щепки"
        self.color = "коричневый"
        self.weight = 4000
        self.width = 12.7
        self.speed = 55

    def get_property(self):
        super().get_property()
        print("количество пушек: " + str(self.number_of_decks) + "\n" +
              "дальность плавания: " + str(self.cruising_range) + " миль" + "\n" +
              "длина: " + str(self.length) + " м" + "\n")


class Destroyer(Ship):
    def __init__(self):
        super().__init__()
        self.drafts = ""
        self.cargo_capacity = ""
        self.engines_type = ""

    def set_property(self):
        super().set_property()
        self.drafts = input("Введите осадки -> ")
        self.cargo_capacity = input("Введите грузовместимость -> ")
        self.engines_type = input("Введите тип двигателя -> ")

    def get_property(self):
        super().get_property()
        print("количество скоростей: " + self.drafts + " т" + "\n" +
              "объем чаши: " + self.cargo_capacity + " т" + "\n" +
              "параметры мощности: " + self.engines_type + "\n")


class Cruiser(Ship):
    def __init__(self, capacity, engine_power, displacement):
        super().__init__()
        self.capacity = capacity
        self.engine_power = engine_power
        self.displacement = displacement

    def get_property(self):
        super().get_property()
        print("вместимость: " + self.capacity + " чел." + "\n" +
              "мощность двигателя: " + self.engine_power + " л.с" + "\n" +
              "водоизмещение: " + self.displacement + " т" + "\n")


ship = Ship()
ship.set_property()
ship.get_property()

frigate = Frigate("28", "5000", "200")
frigate.set_property()
frigate.get_property()

destroyer = Destroyer()
destroyer.set_property()
destroyer.get_property()

сruiser = Cruiser("140", "110000", "9380")
сruiser.set_property()
сruiser.get_property()

