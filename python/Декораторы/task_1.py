import time


def timer(func):
    def render():
        start_time = time.time()
        func()
        end_time = time.time()
        print('Время вычисления: ', execute_time := end_time - start_time)
    return render


@timer
def get_simple_numbers():
    lst = []
    for i in range(2, 1001):
        count = 0
        for j in range(2, 10001):
            if i % j == 0:
                count += 1
        if count > 1:
            pass
        else:
            lst.append(i)
    print(lst)
    return lst


get_simple_numbers()

