import time


def timer(func):
    def render(n, m):
        start_time = time.time()
        func(n, m)
        end_time = time.time()
        print('Время вычисления: ', execute_time := end_time - start_time)
    return render


@timer
def get_simple_numbers(n, m):
    lst = []
    for i in range(n, m):
        if i == 0 or i == 1:
            continue
        count = 0
        for j in range(2, m):
            if j == 0 or j == 1:
                continue
            if i % j == 0:
                count += 1
        if count > 1:
            pass
        else:
            lst.append(i)
    print(lst)
    return lst


left = int(input('Укажите левую границу: '))
right = int(input('Укажите правую границу: '))
get_simple_numbers(left, right)

