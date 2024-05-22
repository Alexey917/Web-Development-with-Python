class Conversion:
    def __init__(self):
        self.metres = int(input("Введите количество метров: "))
        self.menu()

    def menu(self):
        while True:
            menu = input("Выберите тип перевода: "
                         "1-из футов в метры, "
                         "2-из метров в футы, "
                         "3-из ярдов в метры,"
                         "4-из метров в ярды,"
                         "5-из дюймов в метры,"
                         "6-из метров в дюймы \n")

            match menu:
                case "1":
                    print(Conversion.from_feet_to_metres(self.metres))
                    break
                case "2":
                    print(Conversion.from_meters_to_feet(self.metres))
                    break
                case "3":
                    print(Conversion.from_yards_to_metres(self.metres))
                    break
                case "4":
                    print(Conversion.from_meters_to_yards(self.metres))
                    break
                case "5":
                    print(Conversion.from_inches_to_metres(self.metres))
                    break
                case "6":
                    print(Conversion.from_meters_to_inches(self.metres))
                    break
                case _:
                    print("Фиг тебе!")

    @staticmethod
    def from_meters_to_feet(metr):
        res = metr * 3.281
        return round(res, 2)

    @staticmethod
    def from_feet_to_metres(metr):
        res = metr / 3.281
        return round(res, 2)

    @staticmethod
    def from_meters_to_yards(metr):
        res = metr * 1.094
        return round(res, 2)

    @staticmethod
    def from_yards_to_metres(metr):
        res = metr / 1.094
        return round(res, 2)

    @staticmethod
    def from_meters_to_inches(metr):
        res = metr * 39.37
        return round(res, 2)

    @staticmethod
    def from_inches_to_metres(metr):
        res = metr / 39.37
        return round(res, 2)


conversion = Conversion()

