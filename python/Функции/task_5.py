def check(num):
    pol = str(num)
    start = pol[len(pol) // 2::]
    end = pol[:len(pol) // 2:]

    if start == end[::-1]:
        return True
    else:
        return False


print(check(123321))
