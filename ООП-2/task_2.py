class Conversion:
    count = 0

    def __init__(self):
        self.degrees = int(input("Введите температуру: "))
        Conversion.count += 1
        self.menu()

    def menu(self):
        while True:
            menu = input("Выберите тип перевода: "
                         "1-из Цельсия (°C) в Фаренгейт (°F), "
                         "2-из Фаренгейта (°F) в Цельсий (°C), \n")

            match menu:
                case "1":
                    print(self.conversion_to_fahrenheit(self.degrees), "°F")
                    break
                case "2":
                    print(self.conversion_to_celsius(self.degrees), "°C")
                    break
                case _:
                    print("Фиг тебе!")

    @staticmethod
    def conversion_to_fahrenheit(deg):
        res = deg * 1.8 + 32
        return round(res, 2)

    @staticmethod
    def conversion_to_celsius(deg):
        res = (deg - 32) * 1.8
        return round(res, 2)

    @staticmethod
    def object_counting(count):
        return count


conversion = Conversion()
conversion2 = Conversion()
conversion3 = Conversion()
conversion4 = Conversion()

print("Количество подсчетов температуры: ", Conversion.object_counting(Conversion.count))
