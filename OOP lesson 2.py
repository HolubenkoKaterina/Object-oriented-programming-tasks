# Создайте класс Rectangle с атрибутами width и height.
# # Напишите метод, который вычисляет площадь прямоугольника, используя getattr.
# class Rectangle:
#
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def square(self):
#         return self.width * self.height
#
#     def print_resalt(self):
#         return f'square: {self.square()}'
#
# c = Rectangle(5, 150)
# print(c.print_resalt())

# class Rectangle:
#
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def calculate_area(self):
#         return getattr(self, 'width') * getattr(self, 'height')
#
# # Пример использования
# rect = Rectangle(5, 10)
# area = rect.calculate_area()
# print(f"Площадь прямоугольника: {area}")

# Создайте класс Employee с атрибутами name и salary. Напишите метод для удаления атрибута salary с использованием delattr.
# class Employee:
#
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
#
#
# person = Employee('Lili', '50000')
# delattr(person, 'salary')
# print(person.name)

# Создайте класс Circle с атрибутами radius и pi (постоянная).
# Напишите метод для вычисления площади круга с использованием getattr для доступа к radius и pi.

# class Circle:
#
#     def __init__(self, radius, pi=3.14):
#         self.radius = radius
#         self.pi = pi
#     def get_square(self):
#         return self.pi * (self.radius ** 2)
#
# s = Circle(5)
# print(s.get_square())

# class Circle:
#
#     def __init__(self, radius, pi=3.14):
#         self.radius = radius
#         self.pi = pi
#
#     def get_square(self):
#         return getattr(self, 'pi') * (getattr(self, 'radius') ** 2)
#
# s = Circle(5)
# print(s.get_square())

# Создайте класс Student с атрибутами name, age и grades. Напишите метод для добавления оценки
# в список grades с использованием getattr и setattr.
# class Student:
#
#     def __init__(self, name, age, grades):
#         self.name = name
#         self.age = age
#         self.grades = grades
#
#     def add_grade(self, grade):
#         if hasattr(self, 'grades'):
#             self.grades.append(grade)
#         else:
#             self.grades = [grade]
#
#     def get_grades(self):
#         return getattr(self, 'grades', [])
#
# student1 = Student('Lilit', '22', [10, 12, 7])
# student1.add_grade(8)
# print(student1.get_grades())

# Создайте класс BankAccount с атрибутами balance и account_number.
# Реализуйте методы deposit и withdraw, а также метод get_balance, который возвращает баланс.
# class BankAccount:
#
#     def __init__(self, account_number, balance = 0):
#         self.balance = balance
#         self.account_number = account_number
#
#     def deposit(self, amount):
#         self.balance += amount
#
#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#         else:
#             print("Insufficient funds")
#
#     def get_balance(self):
#         return f'balance: {self.balance}'
#
# new_client = BankAccount(account_number='4569')
# new_client.deposit(1000)
# new_client.withdraw(100)
# print(new_client.get_balance())

# Разработайте класс Book с атрибутами title и author. Реализуйте метод get_info, который возвращает информацию о книге.
# class Book:
#
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#
#     def get_info(self):
#         return f'Title: {self.title}, Author: {self.author}'
#
# book1 = Book('Karry', 'King')
# print(book1.get_info())
