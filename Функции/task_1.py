def square(width, symbol, bol):
    for i in range(width):
        for j in range(width):
            if bol:
                print(symbol, end="")
            elif bol == False and (i == 0 or i == width-1 or j == 0 or j == width-1):
                print(symbol, end="")
            else:
                print(" ", end="")

        print("")


square(7, "$", False)
