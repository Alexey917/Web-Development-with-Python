import random

N = int(input("Введите количество строк: "))
M = int(input("Введите количество столбцов: "))

sumTotal = 0
temp = []
sumLst = []

for i in range(N + 1):
    temp.clear()
    for j in range(M):
        temp.append(random.randint(1, 20))
        # Сумма последнего столбца не считается!
        if i != N:
            sumTotal += temp[j]
        else:
            temp[j] = round(sumLst[j] / sumTotal * 100, 2)
            print(temp[j], end="\t")
            continue

        if i == 0:
            sumLst.append(temp[j])
        else:
            sumLst[j] += temp[j]

        print(temp[j], end="\t")
    print("")
print("Сумма элементов всей матрицы: " + str(sumTotal))
