import threading
import time
import random

list_of_num = []


def fill_list():
    for i in range(10):
        list_of_num .append(random.randint(0, 30))
        print(f'[{threading.current_thread().name}] Заполнение списка: элемент {i} -> {list_of_num[i]}')
        time.sleep(1)
    print(f'[{threading.current_thread().name}] Заполненный список: {list_of_num}')


def sum_of_elem():
    s = 0
    for i in list_of_num:
        s += i
    print(f'[{threading.current_thread().name}] Сумма элементов: {s}')
    return s


def mid_of_elem():
    locker.acquire()
    mid = sum_of_elem() / len(list_of_num)
    print(f'[{threading.current_thread().name}] Среднеарифметическое: {mid}')
    return mid


thr1 = threading.Thread(target=fill_list, name='Поток-1')
thr2 = threading.Thread(target=sum_of_elem, name='Поток-2')
thr3 = threading.Thread(target=mid_of_elem, name='Поток-3')
locker = threading.Lock()


thr1.start()
thr1.join()

thr2.start()
thr3.start()

thr2.join()
thr3.join()

print('Finish')

