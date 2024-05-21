def multiplication(start, end):
    mult = 1
    if start < end:
        for i in range(start, end):
            mult *= i
    else:
        for i in range(end, start):
            mult *= i
    return mult


print(multiplication(25, 20))
