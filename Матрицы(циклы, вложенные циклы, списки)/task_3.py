import random

N = int(input("Введите количество строк: "))
M = int(input("Введите количество столбцов: "))
L = int(input("Введите количество строк для поиска нулевых элементов: "))
K = int(input("Введите количество столбцов для поиска нулевых элементов: "))

count = 0
temp = []

for i in range(N):
    temp.clear()
    for j in range(M):
        temp.append(random.randint(0, 20))

        if not i > L-1 and not j > K-1 and temp[j] == 0:
            count += 1

        print(temp[j], end="\t")
    print("")
print("Количество нулевых элементов содержится в L строках и в левых К матрицы: " + str(count))
