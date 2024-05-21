lst = []
with open("files_for_tasks\\task_1_1.txt", encoding='utf-8') as file_1:
    data_1 = file_1.readlines()
    print(data_1)

with open("files_for_tasks\\task_1_2.txt", encoding='utf-8') as file_2:
    data_2 = file_2.readlines()
    print(data_2, "\n")
    for line in data_2:
        if line in data_1:
            pass
        else:
            lst.append(line)
    for line in data_1:
        if line in data_2:
            pass
        else:
            lst.append(line)

print(lst)
print(file_1.closed)
print(file_2.closed)
