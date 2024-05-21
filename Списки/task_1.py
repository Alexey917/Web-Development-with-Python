import random

lst = []
mult = 1
summ = 0
secondLst = []

while True:
    if len(lst) > 9:
        break
    else:
        lst.append(random.randint(-20, 20))

lst.sort()

for i in range(1, len(lst) - 1):
    mult *= lst[i]

print(lst)

for i in range(len(lst)):
    if lst[i] > 0:
        secondLst = lst[i::]
        break

print(secondLst)

for i in range(1, len(secondLst) - 1):
    summ += secondLst[i]

print("Произведение элементов между минимальным и максимальным элементом: " + str(mult))
print("Cумма элементов, находящихся между первым и последним положительными элементами: " + str(summ))
