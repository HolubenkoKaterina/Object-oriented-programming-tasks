# Объявите класс с именем DataBase, который бы хранил в себе следующую информацию:
# pk: 1
# title: "Классы и объекты"
# author: "Имя Фамилия"
# views: 14356
# comments: 12
# Имена переменных (атрибутов класса) используйте такие же (pk, title, author, views и comments) с соответствующими значениями.
# class DataBase:
#     pk = 1
#     title = "Классы и объекты"
#     author = "Имя Фамилия"
#     views = 14356
#     comments = 12

# Объявите класс с именем Goods и пропишите в нем следующие атрибуты (переменные):
# title: "Мороженое"
# weight: 154
# tp: "Еда"
# price: 1024
# Затем, после объявления класса, измените его атрибут price на значение 2048 и добавьте еще один атрибут:
# inflation: 100
# class Goods:
#     title = "Мороженое"
#     weight = 154
#     tp = "Еда"
#     price = 1024
# Goods.price = 2048
# print(Goods.price)
# setattr(Goods, 'price', 2048)
# print(Goods.price)

# Объявите пустой класс с именем Car. С помощью функции setattr() добавьте в этот класс атрибуты:
# model: "Тойота"
# color: "Розовый"
# number: "П111УУ77"
# Выведите на экран значение атрибута color, используя словарь dict класса Car.
# class Car:
#     pass
# setattr(Car, 'model',  "Тойота")
# setattr(Car, 'color', "Розовый")
# setattr(Car, 'number', "П111УУ77")
# print(Car.__dict__)
# print(Car.color)
# print(Car.__dict__['color'])

# Объявите класс с именем Notes и определите в нем следующие атрибуты:
# uid: 1005435
# title: "Шутка"
# author: "И.С. Бах"
# pages: 2
# Затем, с помощью функции getattr() прочитайте и выведите на экран значение атрибута author.
# class Notes:
#     uid = 1005435
#     title = "Шутка"
#     author = "И.С. Бах"
#     pages = 2
# print(getattr(Notes, 'author'))

# Объявите класс с именем Dictionary и определите в нем следующие атрибуты:
# rus: "Питон"
# eng: "Python"
# Затем, с помощью функции getattr() прочитайте и выведите на экран значение атрибута rus_word.
# Если такого атрибута в классе нет, то функция getattr() должна возвращать булево значение False.
# class Dictionary:
#     rus = "Питон"
#     eng = "Python"
# print(getattr(Dictionary, 'rus_word', False))

# Объявите класс с именем TravelBlog и объявите в нем атрибут:
# total_blogs: 0
# Создайте экземпляр этого класса с именем tb1, сформируйте в нем два локальных свойства:
# name: 'Франция'
# days: 6
# Увеличьте значение атрибута total_blogs класса TravelBlog на единицу.
# Создайте еще один экземпляр класса TravelBlog с именем tb2, сформируйте в нем два локальных свойства:
# name: 'Италия'
# days: 5
# Увеличьте значение атрибута total_blogs класса TravelBlog еще на единицу.
# class TravelBlog:
#     total_blogs = 0
#
# tb1 = TravelBlog()
# tb1.name = 'Франция'
# tb1.days = 6
#
# TravelBlog.total_blogs += 1
#
# tb2 = TravelBlog()
# tb2.name = 'Италия'
# tb2.days = 5
#
# TravelBlog.total_blogs += 1

# Объявите класс с именем Figure и двумя атрибутами:
# type_fig: 'ellipse'
# color: 'red'
# Создайте экземпляр с именем fig1 этого класса и добавьте в него следующие локальные атрибуты:
# start_pt: (10, 5)
# end_pt: (100, 20)
# color: 'blue'
# Удалите из экземпляра класса свойство color и выведите на экран список всех локальных свойств
# (без значений) объекта fig1 в одну строчку через пробел в порядке, указанном в задании.
# class Figure:
#     type_fig = 'ellipse'
#     color = 'red'
#
# fig1 = Figure()
# fig1.start_pt = (10, 5)
# fig1.end_pt = (100, 20)
# fig1.color = 'blue'
#
# print(hasattr(fig1, 'color'))
# del fig1.color
# print(fig1.__dict__)

# Объявите класс с именем Person и атрибутами:
# name: 'Имя Фамилия'
# job: 'Программист'
# city: 'Город'
# Создайте экземпляр p1 этого класса и проверьте, существует ли у него локальное свойство с именем job.
# Выведите True, если оно присутствует в объекте p1 и False - если отсутствует.
# class Person:
#     name = 'Имя Фамилия'
#     job = 'Программист'
#     city = 'Город'
#
# p1 = Person()
# print(hasattr(p1, 'job'))

# Объявите класс с именем Student и объявите в нем атрибут:
# total_students: 0
# Создайте экземпляр этого класса с именем student1, сформируйте в нем два локальных свойства:
# name: 'Иван'
# age: 20
# Увеличьте значение атрибута total_students класса Student на единицу.
# class Student:
#     total_students = 0
#
# student1 = Student()
# student1.name = 'Иван'
# student1.age = 20
#
#
# Student.total_students += 1

# Определите класс Dog и объявите в нем атрибут:
# total_dogs: 0
# Создайте экземпляр класса с именем dog1 и установите два локальных свойства:
# name: 'Барон'
# age: 3
# Увеличьте значение атрибута total_dogs класса Dog на единицу.
# class Dog
#     total_dogs = 0
#
# dog1 = Dog()
# dog1.name = 'Барон'
# dog1.age = 3
#
# Dog.total_dogs += 1
