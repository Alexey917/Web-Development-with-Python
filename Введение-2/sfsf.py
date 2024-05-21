number = int(input("Введите число от 0 до 100\n"))

if not(number >= 0 and number <= 100):
  print("Введите другое число")
  number = int(input("Введите число от 0 до 100\n"))