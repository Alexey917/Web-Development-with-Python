number = int(input("Введите число от 0 до 100\n"))

if not(number >= 0 and number <= 100):
  print("Ошибка! Введите другое число")
  number = int(input("Введите число от 0 до 100\n"))

if (number % 3 == 0):
  print("Fizz")
elif (number % 5 == 0):
  print("Buzz")
elif (number % 3 == 0) and (number % 5 == 0):
  print("Fizz Buzz")
else:
  print(number)