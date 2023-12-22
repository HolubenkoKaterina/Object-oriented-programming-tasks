# Объявите класс Book для представления информации о книге. Объекты этого класса
# должны создаваться командами:
# book = Book()
# book = Book(название, автор, число страниц, год издания)
# В каждом объекте класса Book автоматически должны формироваться следующие локальные свойства:
# title - заголовок книги (строка, по умолчанию пустая строка);
# author - автор книги (строка, по умолчанию пустая строка);
# pages - число страниц (целое число, по умолчанию 0);
# year - год издания (целое число, по умолчанию 0).
# Объявите в классе Book магический метод setattr для проверки типов присваиваемых данных
# локальным свойствам title, author, pages и year.
# Если типы не соответствуют локальному атрибуту (например, title должна ссылаться на строку,
# а pages - на целое число), то генерировать исключение командой:
# raise TypeError("Неверный тип присваиваемых данных.")
# Создайте в программе объект book класса Book для книги:
# автор: Имя Фамилия
# заголовок: Python ООП
# pages: 123
# year: 2022
class Book:
#     def __init__(self, title, author, pages, year):
#         self.title = title
#         self.author = author
#         self.pages = pages
#         self.year = year
#
#     @property
#     def get_title(self):
#         return self.title
#
#     @property
#     def get_author(self):
#         return self.author
#
#     @property
#     def get_pages(self):
#         return self.pages
#
#     @property
#     def get_year(self):
#         return self.year
#
#     def __setattr__(self, key, value):
#         if key == 'title' and not isinstance(value, str):
#             raise TypeError("Неверный тип присваиваемых данных.")
#         if key == 'author' and not isinstance(value, str):
#             raise TypeError("Неверный тип присваиваемых данных.")
#         if key == 'pages' and not isinstance(value, int):
#             raise TypeError("Неверный тип присваиваемых данных.")
#         if key == 'year' and not isinstance(value, int):
#             raise TypeError("Неверный тип присваиваемых данных.")
#         else:
#             super().__setattr__(key, value)
#
# book1 = Book('Python ООП', 'Имя Фамилия', 123, 2022)
# print(book1.__dict__)
# book1.title = '5'
# print(book1.title)