# Вам необходимо написать программу описания музеев.
# Для этого нужно объявить класс Museum,
# объекты которого формируются командой:
# mus = Museum(название музея)
# В объектах этого класса должны формироваться
# следующие локальные атрибуты:
# name - название музея (строка);
# exhibits - список экспонатов (изначально пустой список).
# Сам класс Museum должен иметь методы:
# add_exhibit(self, obj) - добавление
# нового экспоната в музей (в конец списка exhibits);
# remove_exhibit(self, obj) - удаление
# экспоната из музея (из списка exhibits по
# ссылке obj - на экспонат)
# get_info_exhibit(self, indx) - получение
# информации об экспонате (строка) по
# индексу списка (нумерация с нуля).


# Экспонаты представляются объектами своих
# классов. Для примера объявите в программе
# следующие классы экспонатов:
# Picture - для картин;
# Mummies - для мумий;
# Papyri - для папирусов.
# Объекты этих классов должны создаваться
# следующим образом (с соответствующим набором
# локальных атрибутов):
# p = Picture(название, художник, описание)
# # локальные атрибуты: name - название;
# author - художник; descr - описание
# m = Mummies(имя мумии, место находки, описание)
# # локальные атрибуты: name - имя мумии;
# location - место находки; descr - описание
# pr = Papyri(название папируса, датировка, описание)
# # локальные атрибуты: name - название папируса;
# date - датировка (строка); descr - описание
# Метод get_info_exhibit() класса Museum должен
# возвращать значение атрибута descr
# указанного экспоната в формате:
#
# "Описание экспоната {name}: {descr}"
#
# Например:
#
# "Описание экспоната Девятый вал: Айвазовский
# написал супер картину."
#
# Пример использования классов (в программе эти
# строчки писать не нужно - только для примера):
#
# mus = Museum("Эрмитаж")
# mus.add_exhibit(Picture("Балакирев с подписчиками
# пишет письмо иноземному султану", "Неизвестный автор",
# "Вдохновляющая, устрашающая, волнующая картина"))
# mus.add_exhibit(Mummies("Балакирев", "Древняя Россия",
# "Просветитель XXI века, удостоенный мумификации"))
# p = Papyri("Ученья для, не злата ради", "Древняя Россия",
# "Самое древнее найденное рукописное свидетельство
# о языках программирования")
# mus.add_exhibit(p)
# for x in mus.exhibits:
#     print(x.descr)

class Museum:
    def __init__(self, name):
        self.name = name
        self.exhibits = []

    def add_exhibit(self, exhibit):
        self.exhibits.append(exhibit)

    def remove_exhibit(self, exhibit):
        self.exhibits.remove(exhibit)

    def get_info_exhibit(self, ind):
        if ind < len(self.exhibits):
            exhibit = self.exhibits[ind]
            return f"Описание экспоната {exhibit.name}: {exhibit.description}"
        else:
            return "Экспонат с таким индексом не найден"

    @property
    def get_name(self):
        return self.name


class Picture:
    def __init__(self, name, author, description):
        self.name = name
        self.author = author
        self.description = description

    @property
    def get_name(self):
        return self.name

    def __str__(self):
        return f'имя: {self.name} автор: {self.author} описание: {self.description}'

class Mummies:
    def __init__(self, name, location, description):
        self.name = name
        self.location = location
        self.description = description

    def __str__(self):
        return f'имя: {self.name} место: {self.location} описание: {self.description}'

    @property
    def get_name(self):
        return self.name

class Papyri:
    def __init__(self, name, date, description):
        self.name = name
        self.date = date
        self.description = description

    @property
    def get_name(self):
        return self.name

    def __str__(self):
        return f'имя: {self.name} дата: {self.date} описание: {self.description}'


mus = Museum("Эрмитаж")
mus.add_exhibit(Picture("Балакирев с подписчиками пишет письмо иноземному султану",
                        "Неизвестный автор",
                        "Вдохновляющая, устрашающая, волнующая картина"))
mus.add_exhibit(Mummies("Балакирев", "Древняя Россия",
                        "Просветитель XXI века, удостоенный мумификации"))
p = Papyri("Ученья для, не злата ради",
           "Древняя Россия",
           "Самое древнее найденное рукописное свидетельство о языках программирования")
mus.add_exhibit(p)
print(mus.exhibits)

for idx, exhibit in enumerate(mus.exhibits):
    print(mus.get_info_exhibit(idx))
