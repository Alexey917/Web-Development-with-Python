import sqlite3
import Databases

db = sqlite3.connect('Sales.db')
sql = db.cursor()  # чтобы делать действия с бд

sql.execute("""CREATE TABLE IF NOT EXISTS Customers (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Surname TEXT NOT NULL
)""")

sql.execute("""CREATE TABLE IF NOT EXISTS Salesmen (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Surname TEXT NOT NULL
)""")

sql.execute("""CREATE TABLE IF NOT EXISTS Sales (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Price INTEGER NOT NULL,
    CustomerId INTEGER NOT NULL,
    SalesmanId INTEGER NOT NULL,
    FOREIGN KEY (CustomerId) REFERENCES Customers (id),
    FOREIGN KEY (SalesmanId) REFERENCES Salesmen (id)
)""")

db.commit()


def fill_data():
    sql.execute("SELECT * FROM Customers")
    if sql.fetchone() is None:
        for i in Databases.customers:
            sql.execute(f"INSERT INTO Customers (name, surname) VALUES('{i.name}', '{i.surname}')")

        for i in Databases.salesmen:
            sql.execute(f"INSERT INTO Salesmen (name, surname) VALUES('{i.name}', '{i.surname}')")

        for i in Databases.sales:
            sql.execute(f"INSERT INTO Sales (Name, Price, CustomerId, SalesmanId) "
                        f"VALUES('{i.name}', '{i.price}', '{i.customerId}', '{i.salesmanId}')")


def insert_data():
    while True:
        choice_db = input("Что хотите добавить? \n"
                          "1-Продавца \n"
                          "2-Покупателя \n"
                          "3-Продажу \n"
                          )

        match choice_db:
            case "1":
                name = input("Имя продавца: ")
                surname = input("фамилия продавца: ")
                new_salesman = Databases.Salesmen(name, surname)
                Databases.customers.append(new_salesman)
                sql.execute(f"INSERT INTO Customers (name, surname) VALUES('{new_salesman.name}', '{new_salesman.surname}')")
                break

            case "2":
                name = input("Имя покупателя: ")
                surname = input("фамилия покупателя: ")
                new_customer = Databases.Customers(name, surname)
                Databases.salesmen.append(new_customer)
                sql.execute(
                    f"INSERT INTO Salesmen (name, surname) VALUES('{new_customer.name}', '{new_customer.surname}')")
                break

            case "3":
                name = input("Название товара: ")
                price = input("Цена: ")
                id_customer = input("Id продавца: ")
                id_salesman = input("Id покупателя: ")
                sale = Databases.Sales(name, price, id_customer, id_salesman)
                Databases.sales.append(sale)
                sql.execute(f"INSERT INTO Sales (Name, Price, CustomerId, SalesmanId) "
                            f"VALUES('{sale.name}', '{sale.price}', '{sale.customerId}', '{sale.salesmanId}')")
                break

            case _:
                print("Фиг тебе!")


def delete_data():
    name = input("Выберите товар для удаления: ")
    counter = 0
    for i in Databases.sales:
        if i.name == name:
            Databases.sales.remove(i)
            del i
            counter += 1
    if counter == 0:
        print('Нет такого товара!\n ')

    sql.execute(f"DELETE FROM Sales WHERE Sales.Name = '{name}'")
    return counter


def update_data():
    name = input("Выберите товар для изменения: ")
    for i in Databases.sales:
        if i.name == name:
            sql.execute(f"UPDATE Sales SET Name = '{input('Имя: ')}', Price = '{input('Цена: ')}',"
                        f"CustomerId = '{input('id продавца: ')}', SalesmanId = '{input('id покуптеля: ')}'"
                        f"WHERE Name = '{name}'")


fill_data()


def display_data():
    for val in sql.execute("SELECT * FROM Customers"):
        print(val)
    print('*' * 40)

    for val in sql.execute("SELECT * FROM Salesmen"):
        print(val)
    print('*' * 40)

    for val in sql.execute("SELECT * FROM Sales"):
        print(val)
    print('*' * 40)


def save_in_file(data):
    with open("results.txt", "a", encoding='utf-8') as file:
        file.write(data + '\n')
        file.write('*'*40 + '\n')


display_data()
db.commit()

with open("results.txt", "w") as file:
    pass

while True:
    print('='*40)
    menu = input("Выберите действие: \n"
                 "1-Отображение всех сделок \n"
                 "2-Отображение сделок конкретного продавца \n"
                 "3-Отображение максимальной по сумме сделки \n"
                 "4-Отображение минимальной по сумме сделки \n"
                 "5-Отображение максимальной по сумме сделки для конкретного продавца \n"
                 "6-Отображение минимальной по сумме сделки для конкретного продавца \n"
                 "7-Отображение максимальной по сумме сделки для конкретного покупателя \n"
                 "8-Отображение минимальной по сумме сделки для конкретного покупателя \n"
                 "9-Отображение продавца, у которого максимальная сумма продаж по всем сделкам \n"
                 "10-Отображение продавца, у которого минимальная сумма продаж по всем сделкам \n"
                 "11-Отображение покупателя, у которого максимальная сумма покупок по всем сделкам \n"
                 "12-Отображение средней суммы покупки для конкретного покупателя \n"
                 "13-Отоображение средней суммы покупки для конкретного продавца \n"
                 "14-Добавить данные в базу \n"
                 "15-Изменить данные \n"
                 "16-Удалить данные \n"
                 "17-выход из меню \n-> ")

    match menu:
        case "1":
            for value in sql.execute("SELECT * FROM Sales"):
                print(value)
                save_in_file(''.join(str(value)))
        case "2":
            customer = input('Введите фамилию продавца: ')
            sql.execute(f"SELECT S.id, S.Name, S.Price, S.SalesmanId, Sm.Name, Sm.Surname FROM Sales as S "
                        f"JOIN Customers as C ON C.id = S.CustomerId "
                        f"JOIN Salesmen as Sm ON Sm.id = S.SalesmanId "
                        f"WHERE C.Surname = '{customer}'")

            count = 0
            for a in sql.fetchall():
                count += 1
                print(a, end='\n')
                save_in_file(''.join(str(a)))

            if count == 0:
                print('Нет такого продавца или у этого продавца нет сделок!')

        case "3":
            for value in sql.execute("SELECT * FROM Sales  ORDER BY Price DESC LIMIT 1"):
                print(value)
                save_in_file(''.join(str(value)))

        case "4":
            for value in sql.execute("SELECT * FROM Sales  ORDER BY Price LIMIT 1"):
                print(value)
                save_in_file(''.join(str(value)))

        case "5":
            customer = input('Введите фамилию продавца: ')
            sql.execute(f"SELECT S.id, S.Name, S.Price, S.SalesmanId, Sm.Name, Sm.Surname FROM Sales as S "
                        f"JOIN Customers as C ON C.id = S.CustomerId "
                        f"JOIN Salesmen as Sm ON Sm.id = S.SalesmanId "
                        f"WHERE C.Surname = '{customer}'"
                        f"ORDER BY S.Price DESC LIMIT 1;")

            count = 0
            for a in sql.fetchall():
                count += 1
                print(a, end='\n')
                save_in_file(''.join(str(a)))

            if count == 0:
                print('Нет такого продавца или у этого продавца нет сделок!')

        case "6":
            customer = input('Введите фамилию продавца: ')
            sql.execute(f"SELECT S.id, S.Name, S.Price, S.SalesmanId, Sm.Name, Sm.Surname FROM Sales as S "
                        f"JOIN Customers as C ON C.id = S.CustomerId "
                        f"JOIN Salesmen as Sm ON Sm.id = S.SalesmanId "
                        f"WHERE C.Surname = '{customer}'"
                        f"ORDER BY S.Price LIMIT 1;")

            count = 0
            for a in sql.fetchall():
                count += 1
                print(a, end='\n')
                save_in_file(''.join(str(a)))

            if count == 0:
                print('Нет такого продавца или у этого продавца нет сделок!')

        case "7":
            salesman = input('Введите фамилию покупателя: ')
            sql.execute(f"SELECT S.id, S.Name, S.Price, S.CustomerId, C.Name, C.Surname FROM Sales as S "
                        f"JOIN Customers as C ON C.id = S.CustomerId "
                        f"JOIN Salesmen as Sm ON Sm.id = S.SalesmanId "
                        f"WHERE Sm.Surname = '{salesman}'"
                        f"ORDER BY S.Price DESC LIMIT 1;")

            count = 0
            for a in sql.fetchall():
                count += 1
                print(a, end='\n')
                save_in_file(''.join(str(a)))

            if count == 0:
                print('Нет такого покупателя или у этого покупателя нет сделок!')

        case "8":
            salesman = input('Введите фамилию покупателя: ')
            sql.execute(f"SELECT S.id, S.Name, S.Price, S.CustomerId, C.Name, C.Surname FROM Sales as S "
                        f"JOIN Customers as C ON C.id = S.CustomerId "
                        f"JOIN Salesmen as Sm ON Sm.id = S.SalesmanId "
                        f"WHERE Sm.Surname = '{salesman}'"
                        f"ORDER BY S.Price  LIMIT 1;")

            count = 0
            for a in sql.fetchall():
                count += 1
                print(a, end='\n')
                save_in_file(''.join(str(a)))

            if count == 0:
                print('Нет такого покупателя или у этого покупателя нет сделок!')

        case "9":
            for value in sql.execute(f"SELECT C.Name, C.Surname FROM Sales as S "
                                     f"JOIN Customers as C ON C.id = S.CustomerId "
                                     f"JOIN Salesmen as Sm ON Sm.id = S.SalesmanId "
                                     f"GROUP BY C.Name ORDER BY  SUM(S.Price) DESC LIMIT 1;"):
                print(value)
                save_in_file(''.join(str(value)))

        case "10":
            for value in sql.execute(f"SELECT C.Name, C.Surname FROM Sales as S "
                                     f"JOIN Customers as C ON C.id = S.CustomerId "
                                     f"JOIN Salesmen as Sm ON Sm.id = S.SalesmanId "
                                     f"GROUP BY C.Name ORDER BY  SUM(S.Price) LIMIT 1;"):
                print(value)
                save_in_file(''.join(str(value)))

        case "11":
            for value in sql.execute(f"SELECT Sm.Name, Sm.Surname FROM Sales as S "
                                     f"JOIN Customers as C ON C.id = S.CustomerId "
                                     f"JOIN Salesmen as Sm ON Sm.id = S.SalesmanId "
                                     f"GROUP BY Sm.Name ORDER BY  SUM(S.Price) DESC LIMIT 1;"):
                print(value)
                save_in_file(''.join(str(value)))

        case "12":
            salesman = input('Введите фамилию покупателя: ')
            sql.execute(f"SELECT AVG(S.Price) FROM Sales as S "
                        f"JOIN Customers as C ON C.id = S.CustomerId "
                        f"JOIN Salesmen as Sm ON Sm.id = S.SalesmanId WHERE Sm.Surname = '{salesman}';")

            count = 0
            for a in sql.fetchall():
                count += 1
                print(a, end='\n')
                save_in_file(''.join(str(a)))

            if count == 0:
                print('Нет такого покупателя или у этого покупателя нет сделок!')

        case "13":
            customer = input('Введите фамилию продавца: ')
            sql.execute(f"SELECT AVG(S.Price) FROM Sales as S "
                        f"JOIN Customers as C ON C.id = S.CustomerId "
                        f"JOIN Salesmen as Sm ON Sm.id = S.SalesmanId WHERE C.Surname = '{customer}';")

            count = 0
            for a in sql.fetchall():
                count += 1
                print(a, end='\n')
                save_in_file(''.join(str(a)))

            if count == 0:
                print('Нет такого покупателя или у этого покупателя нет сделок!')

        case "14":
            insert_data()
            display_data()
            db.commit()

        case "15":
            update_data()
            display_data()
            db.commit()

        case "16":
            res = delete_data()
            if res != 0:
                display_data()
            db.commit()

        case "17":
            break

        case _:
            print("Фиг тебе!")

