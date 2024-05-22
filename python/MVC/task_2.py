from abc import ABC, abstractmethod
import time


class RecipeModel:
    """Рецепт как модель"""
    def __init__(self):
        self.name_of_recipe = 'Бисквит для шоколадного торта'
        self.author = 'Евгений Альдентов'
        self.type = 'Десерт'
        self.description = ("Этот бисквит можно использовать в рецепте "
                            "'Торт Шоколадный бархат' с коньяком рецепт простой")
        self.link = 'https://www.youtube.com/'
        self.ingredients = []
        self.name_of_kitchen = 'советская кухня'

    def add_ingredients(self, *ingredients):
        for i in ingredients:
            self.ingredients.append(i)


class IIngredients:
    """Интерфейс для ингредиентов(паттерн компоновщик)"""
    @abstractmethod
    def get_name(self): pass

    @abstractmethod
    def get_quantity(self): pass


class SimpleIngredients(IIngredients):
    """Реализация простых ингредиентов"""
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def get_name(self): return self.name

    def get_quantity(self): return self.quantity


class CompoundIngredients(IIngredients):
    """Реализация составных ингредиентов"""
    def __init__(self, name):
        self.name = name
        self.quantity = ''
        self.compound = []

    def get_name(self): return self.name

    def get_quantity(self): return self.quantity

    def add_ingredients(self, *ingredient: IIngredients):
        self.compound.append(ingredient)


class DishView:
    """Готовое блюдо и процесс как представление"""

    @staticmethod
    def info(name, obj):
        print('-' * 40 + name + '-' * 40)
        print(f'автор: {obj.author}\n'
              f'тип рецепта: {obj.type}\n'
              f'описание: {obj.description}\n'
              f'ссылка на ютуб: {obj.link}\n'
              f'название кухни: {obj.name_of_kitchen}\n')

    @staticmethod
    def collecting_ingredients(ingredients):
        print('-'*40)
        print('Идет сбор ингредиентов:')
        for i in ingredients:
            print(i.get_name() + ' ' + i.get_quantity())
            time.sleep(0.7)

    @staticmethod
    def combine_dry_ingredients(string): print(f'{'-'*40}\nСоединяем {string}...')

    @staticmethod
    def combine_oil_mixture(string): print(f'{'-'*40}\nДелаем {string}...')

    @staticmethod
    def combine_mixtures(string): print(f'{'-'*40}\nДелаем {string}...')

    @staticmethod
    def mix(): print('-'*40 + '\nПеремешиваем...')

    @staticmethod
    def mixer(): print('-'*40 + '\nИспользуем миксер...')

    @staticmethod
    def beat(): print('-'*40 + '\nВзбиваем...')

    @staticmethod
    def get_vinegar(string): print(f'{'-'*40}\nДобавляем {string}...')

    @staticmethod
    def bake(): print('-'*40 + '\nВыпекаем около 1 ч при 160 °...')

    @staticmethod
    def biscuit_ready(): print('-' * 40 + '\nБисквит готов! Теперь его можно использовть'
                                          ', например,в шоколадном торте.')


class ChefController:
    """Шеф повар, готовящий по рецепту, как контроллер"""
    def __init__(self, model: RecipeModel, view: DishView):
        self.model = model
        self.view = view

    def collecting_ingredients(self):
        """Сбор ингредиентов"""
        egg = SimpleIngredients('яйцо', '2шт')
        sugar = SimpleIngredients('сахар', '250г')
        milk = SimpleIngredients('молоко', '280мл')
        vegetable_oil = SimpleIngredients('растительное масло', '60мл')
        butter = SimpleIngredients('сливочное масло', '60г')
        flour = SimpleIngredients('мука', '240г')
        cocoa = SimpleIngredients('какао', '55г')
        soda = SimpleIngredients('сода', '10г')
        salt = SimpleIngredients('соль', '3г')
        vinegar = SimpleIngredients('уксус (9%)', '12мл')

        self.view.info(self.model.name_of_recipe, self.model)

        # добавляеи ингредиенты в модель
        self.model.add_ingredients(egg, sugar, milk, vegetable_oil, butter,
                                   flour, cocoa, soda, salt, vinegar)

        # отображаем ингредиенты через представление(view)
        self.view.collecting_ingredients(self.model.ingredients)

    def preparing_sponge_cake(self):
        """Приготовление бисквита"""
        dry_ingredients = CompoundIngredients('Cухие ингридиенты')
        dry_ingredients.add_ingredients(self.model.ingredients[1],
                                        self.model.ingredients[5],
                                        self.model.ingredients[6],
                                        self.model.ingredients[7],
                                        self.model.ingredients[8])
        self.view.combine_dry_ingredients(dry_ingredients.get_name())  # Соединить сухие ингредиенты
        time.sleep(2)

        oil_mixture = CompoundIngredients('маслянная смесь')
        oil_mixture.add_ingredients(self.model.ingredients[2],
                                    self.model.ingredients[3],
                                    self.model.ingredients[4],
                                    self.model.ingredients[1])
        self.view.combine_oil_mixture(oil_mixture.get_name())  # Делаем маслянную смесь
        time.sleep(2)
        self.view.mix()
        time.sleep(2)

        dough = CompoundIngredients('тесто')
        dough.add_ingredients(dry_ingredients, oil_mixture)
        self.view.combine_mixtures(dough.get_name())  # Соединиям масляную и сухую смесь
        time.sleep(2)
        self.view.mixer()
        time.sleep(2)

        biscuit = CompoundIngredients('в тесто уксус')
        biscuit.add_ingredients(self.model.ingredients[9])
        self.view.get_vinegar(biscuit.get_name())
        time.sleep(2)
        self.view.beat()
        time.sleep(2)
        self.view.bake()
        time.sleep(2)
        self.view.biscuit_ready()


recipe = RecipeModel()
view = DishView()
chef = ChefController(recipe, view)
chef.collecting_ingredients()
chef.preparing_sponge_cake()
