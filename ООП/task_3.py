class Stadium:
    def __init__(self):
        self.stadium_info = {
            "название": "",
            "дата открытия": "",
            "страна": "",
            "город": "",
            "вместимость": "",
        }

    def input_stadium(self):
        for key, value in self.stadium_info.items():
            self.stadium_info[key] = input(key + ":\t")

    def output_stadium(self):
        for key, value in self.stadium_info.items():
            print(key + ":\t" + value)

    def output_name(self):
        print("Название" + ":\t" + self.stadium_info["название"])

    def output_date(self):
        print("дата открытия" + ":\t" + self.stadium_info["дата открытия"])

    def output_country(self):
        print("страна" + ":\t" + self.stadium_info["страна"])

    def output_city(self):
        print("город" + ":\t" + self.stadium_info["город"])

    def output_capacity(self):
        print("вместимость" + ":\t" + self.stadium_info["вместимость"])


stadium = Stadium()
stadium.input_stadium()
print("\n")
stadium.output_stadium()
print("\n")
stadium.output_name()
stadium.output_date()
stadium.output_country()
stadium.output_city()
stadium.output_capacity()
