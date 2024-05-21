with open("files_for_tasks\\task_4.txt", "r", encoding="utf-8") as file:
    data = file.readlines()
    print(data)
    lst = []
    for line in data:
        lst.append(len(list(line)))
    lst.sort()
    print(lst)
    line_max = lst[len(lst) - 1]
    print(line_max)

