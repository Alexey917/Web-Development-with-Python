firstManager = int(input("Введите уровень продаж  первого менеджера: "))
secondManager = int(input("Введите уровень продаж  второго менеджера: "))
thirdManager = int(input("Введите уровень продаж  третьего менеджера: "))
salaryFirstManager, salarySecondManager, salaryThirdManager = 200, 200, 200

if firstManager < 500:
    salaryFirstManager += firstManager * 0.03
elif (firstManager > 500) and (firstManager < 1000):
    salaryFirstManager += firstManager * 0.05
else:
    salaryFirstManager += firstManager * 0.08

if secondManager < 500:
    salarySecondManager += secondManager * 0.03
elif (secondManager > 500) and (secondManager < 1000):
    salarySecondManager += secondManager * 0.05
else:
    salarySecondManager += secondManager * 0.08

if thirdManager < 500:
    salaryThirdManager += thirdManager * 0.03
elif (thirdManager > 500) and (thirdManager < 1000):
    salaryThirdManager += thirdManager * 0.05
else:
    salaryThirdManager += thirdManager * 0.08


print("Зарплата первого менеджера: "+ str(salaryFirstManager))
print("Зарплата второго менеджера: "+ str(salarySecondManager))
print("Зарплата третьего менеджера: "+ str(salaryThirdManager))

TheBestManager = 0

if salaryFirstManager > salarySecondManager:
    TheBestManager = salaryFirstManager

elif salaryFirstManager < salarySecondManager:
    TheBestManager = salarySecondManager


if TheBestManager < salaryThirdManager:
    TheBestManager = salaryThirdManager
    salaryThirdManager += 200
    print("Лучший менеджер: thirdManager получает премию и его зарплата становится: "+str(salaryThirdManager))

elif TheBestManager == salarySecondManager:
    salarySecondManager += 200
    print("Лучший менеджер: secondManager получает премию и его зарплата становится: "+str(salarySecondManager))

else:
    salaryFirstManager += 200
    print("Лучший менеджер: firstManager получает премию и его зарплата становится: "+str(salaryFirstManager))

