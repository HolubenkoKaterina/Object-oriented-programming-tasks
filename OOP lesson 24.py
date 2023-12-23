# Необходимо написать программу для представления и управления
# расписанием телевизионного вещания.
# Для этого нужно объявить класс TVProgram, объекты
# которого создаются командой:
# pr = TVProgram(название канала)
# где название канала - это строка с названием телеканала.
# В каждом объекте класса TVProgram должен формироваться локальный атрибут:
# items - список из телепередач (изначально список пуст).
# В самом классе TVProgram должны быть реализованы следующие методы:
# add_telecast(self, tl) - добавление новой телепередачи в список items;
# remove_telecast(self, indx) - удаление телепередачи по ее
# порядковому номеру (атрибуту __id, см. далее).
# Каждая телепередача должна описываться классом Telecast,
# объекты которого создаются командой:
# tl = Telecast(порядковый номер, название, длительность)
# где порядковый номер - номер телепередачи в сетке вещания
# (от 1 и далее); название - наименование телепередачи;
# длительность - время телепередачи (в секундах - целое число).
# Соответственно, в каждом объекте класса Telecast
# должны формироваться локальные приватные атрибуты:
# __id - порядковый номер (целое число);
# __name - наименование телепередачи (строка);
# __duration - длительность телепередачи в секундах (целое число).
# Для работы с этими приватными атрибутами в классе
# Telecast должны быть объявлены соответствующие объекты-свойства (property):
# uid - для записи и считывания из локального атрибута __id;
# name - для записи и считывания из локального атрибута __name;
# duration - для записи и считывания из локального атрибута __duration.
# Пример использования классов (эти строчки в программе писать не нужно):
# pr = TVProgram("Первый канал")
# pr.add_telecast(Telecast(1, "Доброе утро", 10000))
# pr.add_telecast(Telecast(2, "Новости", 2000))
# pr.add_telecast(Telecast(3, "Интервью с Балакиревым", 20))
# for t in pr.items:
#     print(f"{t.name}: {t.duration}")

# class CheckTelecastName:
#     def __init__(self, min_len_name, max_len_name):
#         self.min_len_name = min_len_name
#         self.max_len_name = max_len_name
#
#     def __get__(self, instance, owner):
#         return getattr(instance, f"_{owner.__name__}__name")
#
#     def __set_name__(self, owner, name):
#         if not self.min_len_name <= len(name) <= self.max_len_name:
#             raise ValueError('длина имени не соответствует!')
#         if not isinstance(name, str):
#             raise TypeError('Имя должно быть строкой')
#         setattr(owner, f'{owner.__name__}__name', name)
#
#
# class TVProgram:
#
#     def __init__(self, name):
#         self.name = name
#         self.items = []
#
#     def add_telecast(self, tl):
#         self.items.append(tl)
#
#     def remove_telecast(self, tl):
#         self.items.remove(tl)
#
#
# class Telecast:
#     name = CheckTelecastName(1, 20)
#     counter = 0
#
#     def __init__(self, name, duration):
#         Telecast.counter += 1
#         self.id = Telecast.counter
#         self.name = name
#         self.duration = duration
#
#     @property
#     def get_id(self):
#         return self.id
#
#     @property
#     def get_name(self):
#         return self.name
#
#     @property
#     def get_duration(self):
#         return self.duration
#
#
# pr = TVProgram("Первый канал")
# pr.add_telecast(Telecast("Доброе утро", 10000))
# pr.add_telecast(Telecast("Новости", 2000))
# pr.add_telecast(Telecast("Интервью с Балакиревым", 20))
#
# for t in pr.items:
#     print(f"{t.get_name}: {t.get_duration}")
