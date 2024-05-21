numbers = input("Введите набор чисел через пробел:\n-> ")
numbers = numbers.split(" ")
lst = []
for i in numbers:
    i = int(i)
    lst.append(i)

print(lst)


class Node:
    def __init__(self, data=None, nxt=None):
        self.data = data
        self.next = nxt


class OneLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def push_back(self):
        val = int(input("Число для добавления в конец: "))
        if val == self.check_list(val):
            print("В списке уже есть такое значение!")
            return
        node = Node(val)
        if self.head is None:
            self.head = node
        ptr = self.head
        while ptr.data != self.tail.data:
            ptr = ptr.next
        ptr.next = node

        OneLinkedList.print_list(self.head)

    def push_front(self):
        val = int(input("Число для добавления в начало: "))
        if val == self.check_list(val):
            print("В списке уже есть такое значение!")
            return
        node = Node(val)
        if self.head is None:
            self.head = node
        ptr = self.head
        node.next = ptr
        self.head = node
        OneLinkedList.print_list(self.head)

    def insert(self):
        val = int(input("Число для добавления в куда-нибудь, кроме начало и конца: "))
        if val == self.check_list(val):
            print("В списке уже есть такое значение!")
            return
        elem = int(input("Число после которого будет вставка: "))
        node = Node(val)
        if self.head is None:
            self.head = node
        ptr = self.head
        while ptr.data != elem:
            ptr = ptr.next
        if ptr.data == self.tail:
            self.push_back()
        node.next = ptr.next
        ptr.next = node
        OneLinkedList.print_list(self.head)

    def construct(self, li):
        for j in reversed(range(len(li))):
            if j == len(li) - 1:
                self.tail = Node(li[j], self.head)
            self.head = Node(li[j], self.head)
        return self.head

    def check_list(self, value):
        ptr = self.head
        while ptr.data != value:
            if ptr.data == value:
                break
            ptr = ptr.next
            if ptr.next is None:
                break
        return ptr.data

    def check_item(self):
        val = int(input("Число для проверки: "))
        if val == self.check_list(val):
            print("Есть такое значение!")
        else:
            print("Нет такого значения!")

    @staticmethod
    def print_list(head):
        ptr = head
        while ptr is not None:
            print(ptr.data, end=" -> ")
            ptr = ptr.next
        else:
            print("None")


class SecondNode:
    def __init__(self, data=None, nxt=None, prev=None):
        self.data = data
        self.next = nxt
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.past = None

    def delete(self):
        val = int(input("Число для удаления: "))
        ptr = self.head
        right = 0
        while ptr is not None:
            if ptr.data == val and ptr == self.head:
                while ptr.data == val:
                    left = ptr
                    ptr = ptr.next
                    ptr.prev = None
                    self.head = ptr
                    left.next = None

            if ptr.data == val and ptr != self.tail and ptr != self.head:
                while ptr.data == val and ptr != self.tail:
                    left = ptr.prev
                    right = ptr.next
                    temp = ptr
                    ptr = right
                    temp.next = None
                    temp.prev = None
                    left.next = right
                    right.prev = left
                if ptr == self.tail and ptr.data == val:
                    right = ptr
                    ptr = ptr.prev
                    ptr.next = None
                    right.prev = None
                    self.tail = ptr

            if ptr.next == self.tail:
                right = ptr

            if ptr.data == val and ptr == self.tail:
                ptr.prev = None
                right.next = None
                self.tail = right
            ptr = ptr.next

        self.print_list()

    def change(self):
        val = int(input("Число которое нужно заменить: "))
        add = int(input("Число на которое меняем: "))
        ptr = self.head
        right = 0
        while ptr is not None:
            if ptr.data == val and ptr == self.head:
                left = ptr
                ptr = ptr.next
                second = SecondNode(add)
                ptr.prev = second
                self.head = second
                left.next = None
                second.next = ptr

            if ptr.data == val and ptr != self.tail and ptr != self.head:
                while ptr.data == val and ptr != self.tail:
                    left = ptr.prev
                    right = ptr.next
                    temp = ptr
                    ptr = right
                    temp.next = None
                    temp.prev = None
                    second = SecondNode(add)
                    left.next = second
                    second.prev = left
                    second.next = right
                    right.prev = second
                    if submenu != "a":
                        break
                if ptr == self.tail and ptr.data == val:
                    right = ptr
                    ptr = ptr.prev
                    second = SecondNode(add)
                    ptr.next = second
                    second.prev = ptr
                    right.prev = None
                    self.tail = second

            if ptr.next == self.tail:
                right = ptr

            if ptr.data == val and ptr == self.tail:
                ptr = ptr.prev
                self.tail.prev = None
                second = SecondNode(add)
                right.next = second
                second.prev = right
                second.next = None
                self.tail = second
            ptr = ptr.next
        self.print_list()

    def add_in_list(self, li):
        left = 0
        for j in range(len(li)):
            second = SecondNode(li[j])
            if self.head is None:
                self.head = second
                left = self.head
                left.prev = None
            else:
                left.next = second
                second.prev = left
                second.next = None
                left = second
                self.tail = left
        self.print_list()

    def print_list(self):
        ptr = self.head
        print("None ", end="")
        while ptr is not None:
            print("<-", ptr.data, end=" -> ")
            ptr = ptr.next
        else:
            print("None")

    def print_list_reverse(self):
        ptr = self.tail
        print("Вывод списка с конца: ")
        print("None ", end="")
        while ptr is not None:
            print("<-", ptr.data, end=" -> ")
            ptr = ptr.prev
        else:
            print("None")


one_linked = OneLinkedList()
res = one_linked.construct(lst)
OneLinkedList.print_list(res)

doubly_linked = DoublyLinkedList()
doubly_linked.add_in_list(lst)


while True:
    menu = input("Выберите действие: \n"
                 "1-Добавить новое число в список \n"
                 "2-Удалить все вхождения числа из списка \n"
                 "3-Показать содержимое списка \n"
                 "4-Проверить есть ли значение в списке \n"
                 "5-Заменить значение в списке \n"
                 "6-выход из меню \n-> ")

    match menu:
        case "1":
            OneLinkedList.print_list(res)
            one_linked.push_back()
            one_linked.push_front()
            one_linked.insert()

        case "2":
            doubly_linked.print_list()
            doubly_linked.delete()

        case "3":
            doubly_linked.print_list()
            submenu = input("Выберите действие: \n"
                            "a-с начала \n"
                            "b-с конца \n")
            match submenu:
                case "a":
                    doubly_linked.print_list()

                case "b":
                    doubly_linked.print_list_reverse()

                case _:
                    print("Фиг тебе!")

        case "4":
            OneLinkedList.print_list(res)
            one_linked.check_item()

        case "5":
            doubly_linked.print_list()
            submenu2 = input("Выберите действие: \n"
                             "a-только первое вхождение \n"
                             "b-все вхождения \n")

            match submenu2:
                case "a":
                    doubly_linked.change()

                case "b":
                    doubly_linked.change()

                case _:
                    print("Фиг тебе!")

        case "6":
            break
        case _:
            print("Фиг тебе!")