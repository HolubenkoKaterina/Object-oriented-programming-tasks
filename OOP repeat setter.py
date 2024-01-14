# Объявите класс Book для представления информации о книге. Объекты этого класса должны создаваться командами:
#
# book = Book()
# book = Book(название, автор, число страниц, год издания)
# В каждом объекте класса Book автоматически должны формироваться следующие локальные свойства:
#
# title - заголовок книги (строка, по умолчанию пустая строка);
# author - автор книги (строка, по умолчанию пустая строка);
# pages - число страниц (целое число, по умолчанию 0);
# year - год издания (целое число, по умолчанию 0).
#
# Объявите в классе Book магический метод setattr для проверки типов присваиваемых данных локальным свойствам title, author, pages и year.
# Если типы не соответствуют локальному атрибуту (например, title должна ссылаться на строку, а pages - на целое число),
# то генерировать исключение командой:
#
# raise TypeError("Неверный тип присваиваемых данных.")
# Создайте в программе объект book класса Book для книги:
#
# автор: Сергей Балакирев
# заголовок: Python ООП
# pages: 123
# year: 2022

# class Book:
#     def init(self, title="", author="", pages=0, year=0):
#         self._title = title
#         self._author = author
#         self._pages = pages
#         self._year = year
#
#     # @property
#     # def title(self):
#     #     return self._title
#     #
#     # @title.setter
#     # def title(self, title):
#     #     if isinstance(title, str):
#     #         self._title = title
#
#     def setattr(self, key, value):
#         dict_types = {"_title": str, "_author": str, "_pages": int, "_year": int}
#         if not isinstance(value, dict_types[key]):
#             raise ValueError
#         object.setattr(self, key, value)
#
#     def str(self):
#         return " ".join(str(attr) for attr in self.dict.values())


# book = Book("Book1", "Author1", 1000, 2013)
# print(book)


# class Product:
#     def init(self, name, weight, price):
#         self._name = name
#         self._weight = weight
#         self._price = price
#
#     def setattr(self, key, value):
#         dict_types = {"_name": str, "_weight": float, "_price": float}
#         if not isinstance(value, dict_types[key]):
#             raise TypeError
#         object.__setattr__(self, key, value)
#
#     def str(self):
#         return f"Name: {self._name}, Weight:{self._weight}, price: {self._price}"
#
# p1 = Product("milk", 1.5, 32.5)
# print(p1)