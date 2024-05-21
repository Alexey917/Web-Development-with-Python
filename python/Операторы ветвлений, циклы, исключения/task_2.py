numberRange = int(input("Введите диапозон: "))

for i in range(numberRange):
    counter = 0
    for j in range(numberRange):
        if i > 0 and j > 0 and i % j == 0 and i % 1 == 0:
            counter += 1

    if not (counter > 2) and (counter > 0):
        print(i)
