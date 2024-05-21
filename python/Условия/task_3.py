tele2 = 2
megafon = 4
beeline = 6
yota = 3

res = 0
callDuration = int(input())
operator = input()

if operator == "tele2":
  res = callDuration * tele2
elif operator == "megafon":
  res = callDuration * megafon
elif operator == "beeline":
  res = callDuration * beeline
elif operator == "yota":
  res = callDuration * yota
else:
  print("У нас нет такого оператора. Попробуйте еще раз")

print(res)