import threading
import time
import random


path = input('Введите путь к файлу: ')


def fill_file():
    with open(path, 'w') as ff:
        print(f'Запускается поток {threading.current_thread().name}...')
        for i in range(10):
            print(f'Запись {i + 1}-го числа в файл {path}...')
            ff.write(str(random.randint(2, 30)) + '\n')
            time.sleep(0.5)
    print(f'Завершение  потока {threading.current_thread().name}...')


def prime_numbers():
    count = 0
    temp_list = []
    with open(path, 'r') as fpn:
        print(f'Запускается поток {threading.current_thread().name}...')
        print(f'Считывается файл {path}, поиск простого числа...')
        for num in fpn:
            if int(num) == 2:
                temp_list.append(num)
            for j in range(2, int(num)):
                if int(num) % 1 == 0 and int(num) % int(num) == 0 and int(num) % j == 0:
                    count = 0
                    break
                else:
                    count += 1
            if count > 0:
                count = 0
                temp_list.append(num)

        with open('prime_numbers.txt', 'w') as fpn_w:
            print(f'найденные простые числа записываются в prime_numbers.txt...')
            for i in temp_list:
                fpn_w.write(i)
    print(f'Завершение  потока {threading.current_thread().name}...')


def factorial():
    temp_list = []
    with open(path, 'r') as fpn:
        print(f'Запускается поток {threading.current_thread().name}...')
        print(f'Считывается файл {path}, вычисляется факториал...')

        def calc(number):
            if number == 1:
                return 1
            return number * calc(number - 1)

        print(f'факториалы чисел записываются в файл factorial.txt...')
        for num in fpn:
            temp_list.append(calc(int(num)))

        with open('factorial.txt', 'w') as f:
            for i in temp_list:
                f.write(str(i) + '\n')
    print(f'Завершение  потока {threading.current_thread().name}...')


thr1 = threading.Thread(target=fill_file, name='thr-1')
thr2 = threading.Thread(target=prime_numbers, name='thr-2')
thr3 = threading.Thread(target=factorial, name='thr-3')

thr1.start()
thr1.join()

thr2.start()
thr3.start()
thr2.join()
thr3.join()
