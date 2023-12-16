#Необходимо объявить класс Bag (рюкзак), объекты
# которого будут создаваться командой:
# bag = Bag(max_weight)
# где max_weight - максимальный суммарный вес вещей, который
# выдерживает рюкзак (целое число).
# В каждом объекте этого класса должен создаваться локальный приватный атрибут:
# __things - список вещей в рюкзаке (изначально список пуст).
# Сам же класс Bag должен иметь объект-свойство:
# things - для доступа к локальному приватному атрибуту __things
# (только для считывания, не записи).
# Также в классе Bag должны быть реализованы следующие методы:
# add_thing(self, thing) - добавление нового предмета в рюкзак
# (добавление возможно, если суммарный вес (max_weight) не будет превышен,
# иначе добавление не происходит);
# remove_thing(self, indx) - удаление предмета по индексу списка __things;
# get_total_weight(self) - возвращает суммарный вес предметов в рюкзаке.
# Каждая вещь описывается как объект класса Thing и создается командой:
# t = Thing(название, вес)
# где название - наименование предмета (строка); вес - вес предмета
# (целое или вещественное число).
# В каждом объекте класса Thing должны формироваться локальные атрибуты:
# name - наименование предмета;
# weight - вес предмета.
# Пример использования классов (эти строчки в программе писать не нужно):
# bag = Bag(1000)
# bag.add_thing(Thing("Книга по Python", 100))
# bag.add_thing(Thing("Котелок", 500))
# bag.add_thing(Thing("Спички", 20))
# bag.add_thing(Thing("Бумага", 100))
# w = bag.get_total_weight()
# for t in bag.things:
#     print(f"{t.name}: {t.weight}")

class WeihgtDescriptor:
    def __init__(self, min_weight, max_weight):
        self.min_weight = min_weight
        self.max_weight = max_weight


    def __set_name__(self, owner, name):
        self.name = f'_{owner.__name__}__{name}'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

class Bag:
    def __init__(self, max_weight):
        self.max_weight = max_weight
        self.__things = []
        self.total_weight = 0

    @property
    def get_things(self):
        return self.__things

    def add_thing(self, thing):
        if self.max_weight >= self.total_weight + thing.weight:
            self.__things.append(thing)
            self.total_weight += thing.weight
        else:
            raise ValueError('Добавление предмета превысит допустимый вес!')

    def remove_thing(self, indx):
        if 0 <= indx < len(self.__things):
            self.total_weight -= self.__things[indx].weight
            del self.__things[indx]
        else:
            raise IndexError('Индекс выходит за пределы списка предметов')

    def get_total_weight(self):
        return self.total_weight


class Thing:
    name = WeihgtDescriptor(5, 15)
    weight = WeihgtDescriptor(0.5, 15)
    def __init__(self, name, weight):
        self.__weight = weight
        self.name = name

    @property
    def get_weight(self):
        return self.__weight

# Пример использования классов:
bag = Bag(1000)
bag.add_thing(Thing("Книга по Python", 100))
bag.add_thing(Thing("Котелок", 500))
bag.add_thing(Thing("Спички", 20))
bag.add_thing(Thing("Бумага", 100))

w = bag.get_total_weight()
for t in bag.get_things:
    print(f"{t.name}: {t.get_weight}")



