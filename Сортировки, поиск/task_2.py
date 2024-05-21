import random

li_1 = []
li_2 = []
li_3 = []
li_4 = []
li_5 = []

for i in range(5):
    li_1.append(random.randint(1, 50))
    li_2.append(random.randint(1, 50))
    li_3.append(random.randint(1, 50))
    li_4.append(random.randint(1, 50))

temp = li_2 + li_3 + li_4
li_5 += li_1

for i in range(len(temp)):
    count = 0
    for j in range(len(li_5)):
        if temp[i] != li_5[j]:
            count += 1
            if count == len(li_5):
                li_5.append(temp[i])

print(li_1)
print(li_2)
print(li_3)
print(li_4)
print(end="\n")
print(li_5)

print("\nКак бы вы хотели отсортировать список? Выберите a - по убыванию, b - по возрастанию")

while True:
    char = input()

    if char == "a":
        print("Сортировка по убыванию: ")
        # сортировка Шелла
        mid = len(li_5) // 2
        while mid > 0:
            for i in range(mid, len(li_5)):
                current = li_5[i]
                index = i
                while index >= mid and li_5[index - mid] < current:
                    li_5[index] = li_5[index - mid]
                    index -= mid
                    li_5[index] = current

            mid //= 2
        print(li_5)

        try:
            numb = int(input("Введите число: "))
            first = 0
            last = len(li_5) - 1


            def binary_ascending_search(li, left, right):
                middle = (right + left) // 2
                while True:
                    if li[middle] == numb:
                        return middle
                    elif li[middle] > numb:
                        left = middle + 1
                    elif li[middle] < numb:
                        right = middle - 1
                    middle = (right + left) // 2
                    if left > right:
                        print("В этом списке нет такого числа!")
                        return -1

            result = binary_ascending_search(li_5, first, last)
            if result != -1:
                print("Число найдено! Его индекс: ", result)

        except ValueError:
            print("Нужно ввести число! Попробуйте еще раз! ")
        break
    elif char == "b":
        print("Сортировка по возрастанию: ")
        # быстрая сортировка

        def quick_sort(li):
            compare_with_point(li_5, 0, len(li_5) - 1)
            return li

        def compare_with_point(li, left, right):
            if left < right:
                split_point = compare(li, left, right)
                compare_with_point(li, left, split_point - 1)
                compare_with_point(li, split_point + 1, right)

        def compare(li, left, right):
            point = li[left]
            left_mark = left + 1
            right_mark = right
            done = False

            while not done:
                while left_mark <= right_mark and li[left_mark] <= point:
                    left_mark += 1

                while right_mark >= left_mark and li[right_mark] >= point:
                    right_mark -= 1

                if right_mark < left_mark:
                    done = True
                else:
                    li[left_mark], li[right_mark] = li[right_mark], li[left_mark]

            li[left], li[right_mark] = li[right_mark], li[left]
            return right_mark

        res = quick_sort(li_5)
        print(res)

        try:
            numb = int(input("Введите число: "))
            first = 0
            last = len(li_5) - 1

            def binary_ascending_search(li, left, right):
                middle = (right + left) // 2
                while True:
                    if li[middle] == numb:
                        return middle
                    elif li[middle] > numb:
                        right = middle - 1
                    elif li[middle] < numb:
                        left = middle + 1
                    middle = (right + left) // 2
                    if left > right:
                        print("В этом списке нет такого числа!")
                        return -1


            result = binary_ascending_search(li_5, first, last)
            if result != -1:
                print("Число найдено! Его индекс: ", result)

        except ValueError:
            print("Нужно ввести число! Попробуйте еще раз! ")
        break
    else:
        print("или a или b: ")
