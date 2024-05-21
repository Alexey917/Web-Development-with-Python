res = 0
for i in range(1, 11):
    for j in range(1, 11):
        res = i * j
        print(str(i) + " * " + str(j) + " = " + str(res) + "\t\t", end="")
    print("\n")