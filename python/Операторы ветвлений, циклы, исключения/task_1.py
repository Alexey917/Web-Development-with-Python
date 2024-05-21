start = int(input("Введите начало диапозона: "))
end = int(input("Введите конец диапозона: "))

sumEven = 0
sumOdd = 0
sumMultOfNine = 0
quantityEven = 0
quantityOdd = 0
quantityMultOfNine = 0

for i in range(start, end):
    if i % 2 == 0:
        sumEven += i
        quantityEven += 1
    else:
        sumOdd += i
        quantityOdd += 1
    if i % 9 == 0 and i != 0:
        sumMultOfNine += 1
        quantityMultOfNine += 1

print("Сумма четных чисел " + str(sumEven))  #ошибка 0 / 0
print("Сумма нечетных чисел " + str(sumOdd))
print("Сумма кратных 9 чисел " + str(sumMultOfNine))
print("Среднеарифметическое четных чисел " + str(sumEven // quantityEven))
print("Среднеарифметическое нечетных чисел " + str(sumOdd // quantityOdd))
print("Среднеарифметическое кратных 9 чисел " + str(sumMultOfNine // quantityMultOfNine)) #ошибка 0 / 0