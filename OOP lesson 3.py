# Объявите класс с именем MediaPlayer с двумя методами:
# open(file) - для открытия медиа-файла с именем file
# (создает локальное свойство filename со значением аргумента file в объекте класса MediaPlayer)
# play() - для воспроизведения медиа-файла (выводит на экран строку "Воспроизведение <название медиа-файла>")
# Создайте два экземпляра этого класса с именами: media1 и media2.
# Вызовите из них метод open() с аргументом "filemedia1" для объекта media1 и "filemedia2" для объекта media2.
# После этого вызовите через объекты метод play(). При этом, на экране должно отобразиться две строки (без кавычек):
# "Воспроизведение filemedia1"
# "Воспроизведение filemedia2"
# class MediaPlayer:
#
#     def __init__(self):
#         self.filename = None
#
#     def open_file(self, file):
#         self.filename = file
#
#     def play(self):
#         print(f'Воспроизведение {self.filename}')
#
# media1 = MediaPlayer()
# media2 = MediaPlayer()
# media1.open_file('filemedia1')
# media2.open_file('filemedia2')
# media1.play()
# media2.play()











# Объявите класс с именем Graph и методами:
# set_data(data) - передача набора данных data для последующего отображения (data - список числовых данных);
# draw() - отображение данных (в том же порядке, что и в списке data)
# и атрибутом:
# LIMIT_Y = [0, 10]
# Метод set_data() должен формировать локальное свойство data объекта класса Graph.
# Атрибут data должен ссылаться на переданный в метод список.
# Метод draw() должен выводить на экран список в виде строки из чисел,
# разделенных пробелами и принадлежащие заданному диапазону атрибута LIMIT_Y (границы включаются).
# Создайте объект graph_1 класса Graph, вызовите для него метод set_data() и передайте список:
# [10, -5, 100, 20, 0, 80, 45, 2, 5, 7]
# Затем, вызовите метод draw() через объект graph_1. На экране должна появиться строка с соответствующим набором чисел, записанных через пробел.
# Например (вывод без кавычек):
# "10 0 2 5 7"

# class Graph:
#     LIMIT_Y = [0, 10]
#
#     def set_data(self, data):
#         self.data = data
#
#     def draw(self):
#         result = []
#         for element in self.data:
#             if self.LIMIT_Y[0] <= element <= self.LIMIT_Y[1]:
#                 result.append(str(element))
#         print(' '.join(result))
#
# graph_1 = Graph()
# graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
# graph_1.draw()

# Объявите класс Point так, чтобы объекты этого класса можно было создавать командами:
# p1 = Point(10, 20)
# p2 = Point(12, 5, 'red')
# Здесь первые два значения - это координаты точки на плоскости (локальные свойства x, y),
# а третий необязательный аргумент - цвет точки (локальное свойство color).
# Если цвет не указывается, то он по умолчанию принимает значение black.

# Создайте тысячу таких объектов с координатами (1, 1), (3, 3), (5, 5), ... то есть,
# с увеличением на два для каждой новой точки.
# Каждый объект следует поместить в список points (по порядку).
# Для второго объекта в списке points укажите цвет 'yellow'.
# class Point:
#
#     def __init__(self, x, y, color='black'):
#         self.x = x
#         self.y = y
#         self.color = color
#
# p1 = Point(10, 20)
# p2 = Point(12, 5, 'yellow')
# points = []
#
# for i in range(1, 2001, 2):
#     point = Point(i, i)
#     points.append(point)

# Объявите класс Money так, чтобы объекты этого класса можно было создавать следующим образом:
# my_money = Money(100)
# your_money = Money(1000)
# Здесь при создании объектов указывается количество денег,
# которое должно сохраняться в локальном свойстве (атрибуте) money каждого экземпляра класса.
# class Money:
#
#     def __init__(self, amount):
#         self.amount = amount
#
#     def __str__(self):
#         return f'{self.amount}'
#
# my_money = Money(100)
# your_money = Money(1000)
# print(my_money.__str__())