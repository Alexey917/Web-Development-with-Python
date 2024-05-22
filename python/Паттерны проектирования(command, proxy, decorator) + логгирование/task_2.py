from abc import ABC, abstractmethod
from threading import Timer
import random
import pickle
import copy
import logging


logging.basicConfig(level=logging.DEBUG,
                    filename='msg.log',
                    format='%(levelname)s (%(asctime)s): %(message)s (Line: %(lineno)d) [%(filename)s]',
                    datefmt='%d/%m/%Y %I:%M:%S',
                    filemode='w',
                    encoding='utf-8')

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.FileHandler(f"{__name__}.log", mode='w')
formatter = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

class Decorator(ABC):
    ''' Интерфейс декоратора '''
    @abstractmethod
    def update(self): pass


class Operation(ABC):
    '''Абстрактная операция'''
    @abstractmethod
    def operation(self): pass


class Factory(ABC):
    '''Абстрактная фабрика'''
    @abstractmethod
    def choose(self): pass


class WriteToFile(Operation):
    '''Упаковка данных'''
    def __init__(self):
        self.numbers = [0]*10

    def operation(self):
        with open('numbers.bin', 'wb') as file:
            for n in range(len(self.numbers)):
                self.numbers[n] = random.randint(0, 450)
                #file.write(self.numbers[n]) + ' ')
            pickle.dump(self.numbers, file)

        print('Набор чисел в файле numers.bin: ', self.numbers, '\n')
        logger.info(f"Набор чисел в файле 'numers.bin': {self.numbers}")

    def __str__(self):
        return f'{self.numbers}\n'


class GetData(Operation):
    '''Получение данных'''
    def __init__(self):
        self.data = None

    def operation(self):
        try:
            with open('numbers.bin', 'rb') as file:
                self.data = pickle.load(file)
            print('Полученные данные: ', self.data, '\n')
            logger.info(f"Данные получены: {self.data}")
            return self.data
        except FileNotFoundError as e:
            logger.error(f"Такого файла не существует!", exc_info=True)


class SumData(Operation):
    def __init__(self, get_d: GetData):
        self.data = get_d

    def operation(self):
        s = 0
        for i in self.data.data:
            s += i
        print('Сумма чисел: ', s, '\n')
        logger.info(f"Подсчитана сумма чисел: {s}")
        return s


class MultData(Operation):
    def __init__(self, get_d: GetData):
        self.data = get_d

    def operation(self):
        mult = 1
        for i in self.data.data:

            mult *= i
        print('Произведение чисел: ', mult, '\n')
        logger.info(f"Подсчитано произведение чисел: {mult}")
        return mult


class MinData(Operation):
    def __init__(self, get_d: GetData):
        self.data = get_d

    def operation(self):
        res = min(self.data.data)
        print('Минимальное значение: ', res, '\n')
        logger.info(f"Вычислено минимальное значение: {res}")
        return res


class MaxData(Operation):
    def __init__(self, get_d: GetData):
        self.data = get_d

    def operation(self):
        res = max(self.data.data)
        print('Максимальное значение: ', res, '\n')
        logger.info(f"Вычислено максимальное значение: {res}")
        return res


class IPrototype(ABC):
    @abstractmethod
    def clone(self): pass


class Proxy(IPrototype):
    '''Класс для получения доступа  к данным'''
    def __init__(self, get_d: GetData):
        self.proxy = get_d
        self.operation = ""

    def gain_access(self, obj):
        self.operation = obj
        if self.proxy.data is not None:
            print('Данные были получены. Можно выполнить операцию\n')
            logger.info(f"Данные были получены. Можно выполнить операцию")
            self.operation.operation()
        else:
            print('Данные не были получены. Отказ в выполнении операции\n')
            logger.warning(f"Данные не были получены. Отказ в выполнении операции")

    def clone(self):
        return copy.deepcopy(self)


class UpdateData(Decorator):
    ''' Класс декорируемого объекта '''
    def __init__(self, wr: WriteToFile):
        self.data = wr

    def update(self):
        Timer(30, self.data.operation).start()
        logger.info(f"Данные в файле numbers.bin были обновлены(обновление каждые 30 сек.)")


class FactoryOperation(Factory):

    def choose(self):
        received_data = GetData()
        proxy = Proxy(received_data)
        update = UpdateData(write_to)
        while True:
            update.update()

            menu = input("Выберите действие: \n"
                         "1-Получить данные \n"
                         "2-Вычислить сумму данных \n"
                         "3-Умножить данные \n"
                         "4-Определить минимальное значение \n"
                         "5-Определить максимальное значение \n"
                         "6-выход из меню \n-> ")

            match menu:
                case "1":
                    received_data.operation()
                    logger.info(f"Запрос на получение данных")

                case "2":
                    proxy.gain_access(SumData(received_data))
                    logger.info(f"Запрос на сумму чисел")

                case "3":
                    temp_proxy = proxy.clone()
                    temp_proxy.gain_access(MultData(received_data))
                    logger.info(f"Запрос на произведение чисел")

                case "4":
                    temp_proxy = proxy.clone()
                    temp_proxy.gain_access(MinData(received_data))
                    logger.info(f"Запрос минимального значения")

                case "5":
                    temp_proxy = proxy.clone()
                    temp_proxy.gain_access(MaxData(received_data))
                    logger.info(f"Запрос максимального значения")

                case "6":
                    logger.info(f"Пользователь вышел из меню")
                    break

                case _:
                    print('Нужно указать цифру от 1 до 6(включительно)')
                    logger.warning(f"Указан не существующий пункт меню")


write_to = WriteToFile()
write_to.operation()

factory = FactoryOperation()
factory.choose()

# update = UpdateData(write_to, received_data) # применить синглтон
# update.update()


