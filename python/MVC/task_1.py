import random
import time


class ModelShoes:
    def __init__(self):
        self.type = ['мужская', 'женская']
        self.type_shoe = ['кроссовки', 'сапоги', 'сандалии', 'туфли']
        self.color = ['коричневый', 'белый', 'черный', 'серый', 'синий']
        self.price = random.randint(1000, 10000)
        self.manufacturer = ['Nike', 'Addidas', 'Колесник', 'Superfit']
        self.size = [37, 38, 39, 40, 41, 42, 43, 44, 45]


class ViewShoes:
    @staticmethod
    def display_dialog(value):
        print('-'*40)
        print(value)

    @staticmethod
    def order(li, price):
        print(f'Проверьте ваш заказ:')
        for i in range(0, len(li)):
            print(li[i])
        print('-' * 40)
        print(f'Итого: {price} руб.')
        print('-' * 40)
        print(f'Оплатить заказ:\n'
              f'0 - оплатить\n'
              f'1 - назад\n->')

    @staticmethod
    def success():
        print('Заказ прошел успешно!')


class ControllerShoes:
    def __init__(self):
        self.view = ViewShoes()
        self.model = ModelShoes()

    def set_dict(self):
        dict_shoes = {
            'Хотите сделать заказ?(да/нет):': ['да', 'нет'],
            'Выберите тип обуви:': self.model.type,
            'Выберите вид обуви:': self.model.type_shoe,
            'Цвет обуви:': self.model.color,
            'Выберите производителя:': self.model.manufacturer,
            'Выберите размер:': self.model.size
        }
        return dict_shoes

    @staticmethod
    def user_answer(value):
        while True:
            answer = user.give_answer()
            if answer >= len(value) or answer < 0:
                print(f'Нет такого пункта! Попробуйте еще раз!')
            else:
                break
        return answer

    def user_pay(self):
        while True:
            pay = user.pay()
            if pay == 1:
                return pay
            elif pay == 0:
                self.view.success()
                return pay
            else:
                print(f'Нет такого пункта! Попробуйте еще раз!')

    def menu(self):
        collect_order = []
        while True:
            collect_order.clear()
            for key, val in self.set_dict().items():
                self.view.display_dialog(key)
                for i in range(len(val)):
                    self.view.display_dialog(f'{i} - {val[i]}')
                self.view.display_dialog('->')
                res = self.user_answer(val)
                if key == 'Хотите сделать заказ?(да/нет):':
                    if res == 1:
                        return False
                    else:
                        continue
                collect_order.append(val[res])
            self.view.order(collect_order, self.model.price)
            self.user_pay()
            time.sleep(0.7)


class User:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @staticmethod
    def order_shoes(obj):
        obj.menu()

    @staticmethod
    def give_answer():
        answer = int(input())
        return answer

    @staticmethod
    def pay():
        pay = int(input())
        return pay


user = User('Фома', 'Верующий')
controller = ControllerShoes()
user.order_shoes(controller)
