'''Используется Абстрактная фабрика и фабричный метод'''

from abc import ABC, abstractmethod


class PastaFactory(ABC):
    @abstractmethod
    def cooking_pasta(self):
        """Приготовление пасты"""
        pass


class Pasta(ABC):
    @abstractmethod
    def add_type_pasta(self):
        """Тип пасты"""
        pass

    @abstractmethod
    def add_sauce(self):
        """Соус"""
        pass

    @abstractmethod
    def add_filling(self):
        """Начинка"""
        pass

    @abstractmethod
    def add_supplements(self):
        """Добавки"""
        pass


class Carbonara(Pasta):
    def __init__(self):
        self.spaghetti: str = ''

        self.olive_oil: str = ''
        self.yolk: str = ''
        self.butter: str = ''

        self.egg: str = ''
        self.brisket: str = ''
        self.cheese: str = ''

        self.garlic: str = ''

    def add_type_pasta(self):
        self.spaghetti: str = 'спагетти'
        print('добавялем: ' + self.spaghetti)
        return self

    def add_sauce(self):
        self.olive_oil: str = 'оливковое масло 2 ст.л., '
        self.yolk: str = 'желток 3шт., '
        self.butter: str = 'сливочное масло 1 ст.л., '
        print('готовим соус: ' + self.olive_oil, self.yolk, self.butter)
        return self

    def add_filling(self):
        self.egg: str = 'яйцо 1 шт., '
        self.brisket: str = 'грудинка 200г., '
        self.cheese: str = 'сыр пормезан 75г., '
        print('добавялем начинку: ' + self.egg, self.brisket, self.cheese)
        return self

    def add_supplements(self):
        self.garlic: str = 'чеснок 2 зубчика'
        print('добавялем: ' + self.garlic + '\n')
        return self


class Fetuchini(Pasta):
    def __init__(self):
        self.fetuchini: str = ''

        self.olive_oil: str = ''
        self.cream: str = ''
        self.hard_cheese: str = ''

        self.bacon: str = ''
        self.chicken_fillet: str = ''
        self.onion: str = ''

        self.basil: str = ''

    def add_type_pasta(self):
        self.fetuchini: str = 'фетучини'
        print('добавялем: ' + self.fetuchini)
        return self

    def add_sauce(self):
        self.olive_oil: str = 'оливковое масло 3 ст.л., '
        self.cream: str = 'сливки 250гр., '
        self.hard_cheese: str = 'твердый сыр 50гр., '
        print('готовим соус: ' + self.olive_oil, self.cream, self.hard_cheese)
        return self

    def add_filling(self):
        self.bacon: str = 'бекон 50г., '
        self.chicken_fillet: str = 'куриное филе 300г., '
        self.onion: str = 'лук 1шт., '
        print('добавялем начинку: ' + self.bacon, self.chicken_fillet, self.onion)
        return self

    def add_supplements(self):
        self.basil: str = 'базилик 8 листк.'
        print('добавялем: ' + self.basil + '\n')
        return self


class Orecchiette(Pasta):
    def __init__(self):
        self.orecchiette: str = ''

        self.tomato_sauce: str = ''

        self.veal: str = ''
        self.tomatoes: str = ''
        self.pecorino_romano: str = ''

        self.chilli: str = ''
        self.dry_red_wine: str = ''
        self.salt = ''

    def add_type_pasta(self):
        self.orecchiette: str = 'ореккьетте'
        print('добавялем: ' + self.orecchiette)
        return self

    def add_sauce(self):
        self.tomato_sauce: str = 'томатный соус 240гр., '
        print('готовим соус: ' + self.tomato_sauce)
        return self

    def add_filling(self):
        self.veal: str = 'телятина 100гр., '
        self.tomatoes: str = 'помидоры 500гр., '
        self.pecorino_romano: str = 'сыр пекорино романо  20гр., '
        print('добавялем начинку: ' + self.veal, self.tomatoes, self.pecorino_romano)
        return self

    def add_supplements(self):
        self.chilli: str = 'перец чили 6гр., '
        self.dry_red_wine: str = 'красное сухое вино 200мл., '
        self.salt: str = 'соль по вкусу'
        print('добавялем: ' + self.chilli + self.dry_red_wine + self.salt + '\n')
        return self


class CookingPasta(PastaFactory):
    def cooking_pasta(self):
        menu = input("Выберите пасту: \n"
                     "1-Карбонара \n"
                     "2-Фетучини \n"
                     "3-Ореккьетте \n-> ")

        match menu:
            case "1":
                print('Начинаем готовить пасту карбонара...\n')
                carbonara = Carbonara()
                carbonara.add_type_pasta().add_sauce().add_filling().add_supplements()
                print('Паста готова! Садитесь жрать, пожалуйста!\n')
                return carbonara

            case "2":
                print('Начинаем готовить пасту фетучини...\n')
                fetuchini = Fetuchini()
                fetuchini.add_type_pasta().add_sauce().add_filling().add_supplements()
                print('Паста готова! Садитесь жрать, пожалуйста!\n')
                return fetuchini

            case "3":
                print('Начинаем готовить пасту ореккьетте...\n')
                orecchiette = Orecchiette()
                orecchiette.add_type_pasta().add_sauce().add_filling().add_supplements()
                print('Паста готова! Садитесь жрать, пожалуйста!\n')
                return orecchiette

            case _:
                print('Нужно выбрать число соответсвующее виду пасты')


cook = CookingPasta()
cook.cooking_pasta()

cook1 = CookingPasta()
cook1.cooking_pasta()

cook2 = CookingPasta()
cook2.cooking_pasta()


