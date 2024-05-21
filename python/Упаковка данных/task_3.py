import pickle
import json
from datetime import datetime


class Stadium:
    def __init__(self):
        self.stadium_info = {
            "название": "",
            "дата открытия": "",
            "страна": "",
            "город": "",
            "вместимость": "",
        }

    def __str__(self):
        return (f"Название: {self.stadium_info['название']}\n"
                f"Год выпуска: {self.stadium_info['дата открытия']}\n"
                f"дата открытия: {self.stadium_info['страна']}\n"
                f"город: {self.stadium_info['город']}\n"
                f"вместимость: {self.stadium_info['вместимость']}\n")

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
        print("вместимость" + ":\t" + self.stadium_info["вместимость"]+'\n')

    @staticmethod
    def serialization_bin(obj):
        with open('for_task_3.bin', 'wb') as file:
            pickle.dump(obj, file)

    @staticmethod
    def deserialization_bin():
        with open('for_task_3.bin', 'rb') as file:
            data = pickle.load(file)
            print(data, '\n')

    def serialization_json(self):
        with open('for_task_3.json', 'w') as file:
            json.dump(self.stadium_info, file)

    @staticmethod
    def deserialization_json():
        with open('for_task_3.json', 'r') as file:
            data = json.load(file)
            print(data, '\n')


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

start_time = datetime.now()
Stadium.serialization_bin(stadium)
Stadium.deserialization_bin()
end_time = datetime.now()
execution_time = end_time - start_time

start_time2 = datetime.now()
Stadium.serialization_json(stadium)
Stadium.deserialization_json()
end_time2 = datetime.now()
execution_time2 = end_time2 - start_time2

print('Время работы с использованием pickle:', execution_time)
print('Время работы с использованием json:', execution_time)