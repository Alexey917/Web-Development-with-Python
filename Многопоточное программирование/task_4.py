import threading
import os
import re


def search_in_files():
    print(f'Запускается поток [{threading.current_thread().name}]...')
    if os.path.exists('for_task_4\\merge.txt'):
        os.remove('for_task_4\\merge.txt')
    else:
        pass
    print(f'[{threading.current_thread().name}] - поиск слова...')
    for file in os.listdir(path):
        if file == 'ban.txt':
            continue
        with open(f'{path}\\{file}', 'r', encoding='utf-8') as f:
            for word in f.readlines():
                if word_search in word:
                    with open('for_task_4\\merge.txt', 'a', encoding='utf-8') as f_a:
                        print(f'[{threading.current_thread().name}] - слово найдено, '
                              f'производиться слияние содержимого файла с файлом merge.txt')
                        f.seek(0)
                        f_a.write(f.read()+'\n')
    print(f'Поток [{threading.current_thread().name}] завершает свою работу...')


def cut_words():
    print(f'Запускается поток [{threading.current_thread().name}]...')
    with open('for_task_4\\merge.txt', 'r', encoding='utf-8') as f1:
        print(f'[{threading.current_thread().name}] - считывается файл с запрещенными словами и формируется список...')
        with open('for_task_4\\ban.txt', 'r', encoding='utf-8') as f2:
            ban_list = []
            for line in f2.readlines():
                for word in line.split(' '):
                    ban_list.append(word[:len(word)-1])
            print(ban_list)

            merge_list = []
            with_marks = []  # со знаками препинания и символами
            pattern = r'[!@#№$%^&*()\-\_+=:;\"\'\\|\?/>\.<<`~,]'
            pattern2 = r'\.'
            print(f'[{threading.current_thread().name}] - считывается файл merge.txt и '
                  f'формируется список без знаков препинания и символов конца строки...')
            for line in f1.readlines():
                for word in line.split(' '):
                    if word[len(word)-1] == '\n' or re.search(pattern, word):
                        if re.search(pattern2, word):
                            merge_list.append(word[:len(word) - 2])
                        else:
                            merge_list.append(word[:len(word)-1])
                    else:
                        merge_list.append(word)
                    with_marks.append(word.lower())
            print(merge_list)

            print(f'[{threading.current_thread().name}] - удаление запрещенных слов без знаков и символов...')
            del_list = []
            for i in ban_list:
                for j in merge_list:
                    if i == j:
                        merge_list.remove(j)
                        del_list.append(j)
            print(merge_list)

            print(f'[{threading.current_thread().name}] - удаление запрещенных слов со знаками и символами...')
            for i in del_list:
                for j in with_marks:
                    if j[len(j) - 1] == '\n' or re.search(pattern, j):
                        if re.search(pattern2, j):
                            if i == j[:len(j) - 2]:
                                with_marks.remove(j)
                        else:
                            if i == j[:len(j) - 1]:
                                with_marks.remove(j)
                    else:
                        if i == j:
                            with_marks.remove(j)
            print(with_marks)

    print(f'[{threading.current_thread().name}] - запись изменного текста обратно в merge.txt...')
    with open('for_task_4\\merge.txt', 'w', encoding='utf-8') as f3:
        for i in with_marks:
            if i[len(i)-1] == '\n':
                f3.write(i)
            else:
                f3.write(i + ' ')
    print(f'Поток [{threading.current_thread().name}] завершает свою работу...')


while True:
    path = input('Введите путь к существующей директории\n->')
    if os.path.isdir(path):
        break
    else:
        print("Нет такой директории!Попобуйте еще раз")

word_search = input('Введите слово для поиска: ')

thr1 = threading.Thread(target=search_in_files, name='A')
thr2 = threading.Thread(target=cut_words, name='B')

thr1.start()
thr1.join()
thr2.start()
thr2.join()


