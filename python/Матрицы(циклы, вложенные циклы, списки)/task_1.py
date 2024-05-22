import random

N = int(input("Введите количество строк: "))
M = int(input("Введите количество столбцов: "))

temp = []
sumLst = []

for i in range(N+1):
    temp.clear()
    sumM = 0
    for j in range(M+1):
        temp.append(random.randint(1, 20))

        if i == N:
            temp[j] = sumLst[j] // N
            print(temp[j], end="\t")
            continue

        if j == M:
            temp[j] = sumM // M

        sumM += temp[j]

        if i == 0:
            sumLst.append(temp[j])
        else:
            sumLst[j] += temp[j]

        print(temp[j], end="\t")
    print("")

