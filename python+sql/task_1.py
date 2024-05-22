import pymysql

try:
    connection = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='e38-d2UB!4h',
        cursorclass=pymysql.cursors.DictCursor
    )
    print("successfully connected...")
    print("#" * 20)

    try:
        with connection.cursor() as cursor:
            # cursor.execute('CREATE DATABASE Sales')
            cursor.execute('USE Sales')
            sales_table = ("CREATE TABLE `Sales`(id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,"
                           "Name VARCHAR(100) NOT NULL UNIQUE,"
                           "Price DECIMAL NOT NULL,"
                           "CustomerId INT NOT NULL,"
                           "SalesmanId INT NOT NULL,"
                           "CONSTRAINT CK_Sales_Price CHECK(Price > 0))"
                           )
            cursor.execute(sales_table)
            print("Table created successfully")

    finally:
        connection.close()

except Exception as ex:
    print("Connection refused...")
    print(ex)


# " CONSTRAINT FK_Sales_CustomerId FOREIGN KEY(CustomerId) REFERENCES Customers(id),"
# " CONSTRAINT FK_Sales_SalesmanId FOREIGN KEY(SalesmanId) REFERENCES Salesmen(id));"