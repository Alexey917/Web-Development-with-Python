class Customers:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Salesmen:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Sales:
    def __init__(self, name, price, customers_id, salesman_id):
        self.name = name
        self.price = price
        self.customerId = customers_id
        self.salesmanId = salesman_id


customer_1 = Salesmen('Борис', 'Лисичкин')
customer_2 = Salesmen('Олег', 'Пирожочкин')
customer_3 = Salesmen('Анастасия', 'Хлебушкина')
customer_4 = Salesmen('Анатолий', 'Булочкин')
customer_5 = Salesmen('Екатерина', 'Лавашкина')

customers = [customer_1, customer_2, customer_3, customer_4, customer_5]

salesman_1 = Customers('Евгений', 'Лесной')
salesman_2 = Customers('Владимир', 'Шишкин')
salesman_3 = Customers('Наталия', 'Грибкова')
salesman_4 = Customers('Татьяна', 'Овод')
salesman_5 = Customers('Тереньтий', 'Тетерев')
salesman_6 = Customers('Иван', 'Клещ')
salesman_7 = Customers('Юрий', 'Палатка')
salesman_8 = Customers('Анна', 'Соснова')

salesmen = [salesman_1, salesman_2, salesman_3, salesman_4, salesman_5, salesman_6, salesman_7, salesman_8]

sale_1 = Sales('ноутбук ASUS', 77000, 1, 6)
sale_2 = Sales('ноутбук Baikal', 37000, 2, 5)
sale_3 = Sales('ютуг', 10300, 3, 8)
sale_4 = Sales('клавиатура', 3500, 1, 1)
sale_5 = Sales('наушники', 2700, 2, 3)
sale_6 = Sales('микрофон', 2100, 3, 4)
sale_7 = Sales('пылесос', 19500, 1, 2)
sale_8 = Sales('кот', 1500, 2, 7)
sale_9 = Sales('SSD диск 1TB', 7200, 3, 2)
sale_10 = Sales('HDD диск 2TB', 6500, 1, 7)
sale_11 = Sales('Компьютер', 105000, 2, 5)
sale_12 = Sales('Электрочайник', 12000, 3, 1)
sale_13 = Sales('телевизор', 22400, 1, 8)
sale_14 = Sales('nokia 3310', 1000, 2, 3)
sale_15 = Sales('холодильник', 60000, 3, 6)

sales = [sale_1, sale_2, sale_3, sale_4, sale_5, sale_6, sale_7, sale_8, sale_9, sale_10, sale_11, sale_12, sale_13,
         sale_14, sale_15]


