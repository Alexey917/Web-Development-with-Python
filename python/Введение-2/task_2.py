number = int(input())
newNumber = 1
for i in range(len(str(number))):
    newNumber *= number % 10
    number //= 10

print(newNumber)
