# Вы создаете телефонную записную книжку. Она определяется классом PhoneBook. Объекты этого класса создаются командой:
# p = PhoneBook()
# А сам класс должен иметь следующий набор методов:
# add_phone(phone) - добавление нового номера телефона (в список);
# remove_phone(indx) - удаление номера телефона по индексу списка;
# get_phone_list() - получение списка из объектов всех телефонных номеров.
# Каждый номер телефона должен быть представлен классом PhoneNumber. Объекты этого класса должны создаваться командой:
# note = PhoneNumber(number, fio)
# где number - номер телефона (число) в формате XXXXXXXXXXX (одиннадцати цифр, X - цифра); fio - Ф.И.О. владельца номера (строка).
# В каждом объекте класса PhoneNumber должны формироваться локальные атрибуты:
# number - номер телефона (число);
# fio - ФИО владельца номера телефона.
# Необходимо объявить два класса PhoneBook и PhoneNumber в соответствии с заданием.
# Пример использования классов (эти строчки в программе писать не нужно):
# p = PhoneBook()
# p.add_phone(PhoneNumber(12345678901, "Сергей Балакирев"))
# p.add_phone(PhoneNumber(21345678901, "Панда"))
# phones = p.get_phone_list()



# class PhoneNumber:
#     def __init__(self, number, fio):
#         if PhoneNumber.check_number(number) and PhoneNumber.check_fio(fio):
#             self.__number = number
#             self.__fio = fio
#         else:
#             self.__number = None
#             self.__fio = ""
#
#     @staticmethod
#     def check_number(number):
#         return isinstance(number, int) and len(str(number)) == 10
#
#     @staticmethod
#     def check_fio(fio):
#         return isinstance(fio, str)
#
#     def __str__(self):
#         return f"{self.__number}, {self.__fio}"
#
#
# class PhoneBook:
#     def __init__(self):
#         self.__book = []
#
#     def add_phone(self, phone: PhoneNumber):
#         self.__book.append(phone)
#
#     def remove_phone(self, index):
#         self.__book.pop(index)
#
#     @property
#     def book(self):
#         return self.__book
#
#
# p = PhoneBook()
# p.add_phone(PhoneNumber(1234567891, "Sergei"))
# p.add_phone(PhoneNumber(45681257465684, "Mariia"))
# phones = p.book
# print(*phones)