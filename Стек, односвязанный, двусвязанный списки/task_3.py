import re


class Node:
    count = 0

    def __init__(self, data=None, nxt=None):
        self.data = data
        self.next = nxt
        Node.count += 1


class Stack:
    def __init__(self):
        self.top = None

    def push(self):
        pattern = r'[^\s+]'
        string = input("Введите строку: ")
        while not re.match(pattern, string):
            string = input("Введите хоть что-нибудь, кроме пробелов: ")

        #if Node.count < 5: - больше нет ограничения по элементам
        self.top = Node(string, self.top)
        #else:
           # print("Стек переполнен!")

    def pop(self):
        ptr = self.top
        self.top = ptr.next
        ptr.next = None
        Node.count -= 1
        return ptr.__dict__

    def empty(self):
        if self.top is None:
            print("Стек пуст!")
            return True
        else:
            print("Стек не пустой!")
            return False

    def stack_clear(self):
        while Node.count > 0:
            self.pop()
        else:
            print("Стек очищен!")

    def get_top(self):
        return f'{"data", self.top.data}', f'{"next", self.top.next.data}'

    def print_stack(self):
        ptr = self.top
        while ptr is not None:
            print(ptr.data, "\n|\nv")
            ptr = ptr.next
        else:
            print("None")


stack = Stack()
stack.push()
stack.print_stack()
while True:
    menu = input("\nВыберите действие: \n"
                 "1-помещение строки в стек \n"
                 "2-выталкивание строки из стека \n"
                 "3-подсчет количества строк в стеке \n"
                 "4-проверку пустой стек или полный \n"
                 "5-очистку стека \n"
                 "6-получение значения без выталкивания верхней строки из стека \n"
                 "7-выход из меню \n-> ")

    match menu:
        case "1":
            stack.push()
            stack.print_stack()

        case "2":
            print("Выталкнули: ", stack.pop())
            stack.print_stack()

        case "3":
            print("Количество строк в стеке: ", Node.count)
            stack.print_stack()

        case "4":
            stack.empty()
            stack.print_stack()

        case "5":
            stack.stack_clear()
            stack.print_stack()

        case "6":
            print(stack.get_top())
            stack.print_stack()
        case _:
            print("Фиг тебе!")