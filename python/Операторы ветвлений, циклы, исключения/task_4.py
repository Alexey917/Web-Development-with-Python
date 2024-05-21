height = int(input("Введите высоту ромба: "))


for i in range(height):
    print(" " * (height - i), "*" * (2 * i + 1))

for i in range(height, -1, -1):
    print(" " * (height - i), "*" * (2 * i + 1))