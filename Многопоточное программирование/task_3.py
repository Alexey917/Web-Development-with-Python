import threading
import os
import shutil

while True:
    path = input('Введите существующую директорию: ')
    dst = input('Введите новую директорию : ')
    if os.path.isdir(path):
        if os.path.isdir(dst):
            raise FileExistsError(f'Невозможно создать файл, так как он уже существует!')
        break
    else:
        print("Нет такой директории!Попобуйте еще раз")


def copy():
    print(f'Запускается поток {threading.current_thread().name}...')
    print(f'создается новая директория...')
    print(f'Копируются файлы из указанной нами директории в новую...')
    shutil.copytree(path, dst)
    print(f'Завершение  потока {threading.current_thread().name}...')


thr = threading.Thread(target=copy, name='thr').start()
