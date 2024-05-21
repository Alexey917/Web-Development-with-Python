count = 0
with open("files_for_tasks\\task_3_1.txt", "r", encoding='utf-8') as f1:
    with open("files_for_tasks\\task_3_2.txt", "w", encoding='utf-8') as f2:
        data = f1.readlines()
        print(data)
        data.remove(data[len(data) - 1])
        print(data)
        data_2 = "".join(data)
        print(data_2)
        f2.write(data_2)

