lst_vowels = ["а", "е", "ё", "и", "о", "у", "э", "ю", "я"]
lst_consonants = ["б", "в", "г", "д", "ж", "з", "й", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х", "ц", "ч", "ш", "щ"]
lst_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
count_vowels = 0
count_consonants = 0
count_numbers = 0

with open("files_for_tasks\\task_2_2.txt", "w", encoding='utf-8') as f1:
    with open("files_for_tasks\\task_2_1.txt", "r", encoding='utf-8') as f2:
        count_symbols = len(f2.read())
        f2.seek(0)
        data = f2.read()
        print(data)
        f2.seek(0)
        count_lines = len(f2.readlines())
        print("Количество символов: ", count_symbols)
        print("Количество строк: ", count_lines)
        f1.write("Количество символов: " + str(count_symbols) + "\n")
        f1.write("Количество строк: " + str(count_lines) + "\n")
        f2.seek(0)

        for i in range(len(data)):
            if data[i].lower() in lst_vowels:
                count_vowels += 1
        f1.write("Количество гласный букв: " + str(count_vowels) + "\n")
        print("Количество гласный букв: ", count_vowels)

        for i in range(len(data)):
            if data[i].lower() in lst_consonants:
                count_consonants += 1
        f1.write("Количество согласных букв: " + str(count_consonants) + "\n")
        print("Количество согласных букв: ", count_consonants)

        for i in range(len(data)):
            if data[i] in lst_numbers:
                count_numbers += 1
        f1.write("Количество цифр: " + str(count_numbers))
        print("Количество цифр: ", count_numbers)


