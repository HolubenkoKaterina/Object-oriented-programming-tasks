# Объявите класс-декоратор InputValues с параметром render - функция или объект для преобразования данных из строк в другой тип данных. Чтобы реализовать такой декоратор в инициализаторе init() следует указать параметр render, а магический метод call() определяется как функция-декоратор:
#
# class InputValues:
#     def init(self, render):     # render - ссылка на функцию или объект для преобразования
#         # здесь строчки программы
#
#     def call(self, func):     # func - ссылка на декорируемую функцию
#         def wrapper(*args, **kwargs):
#             # здесь строчки программы
#         return wrapper
# В качестве рендера объявите класс с именем RenderDigit, который бы преобразовывал строковые данные в целые числа. Объекты этого класса создаются командой:
#
# render = RenderDigit()
# и применяются следующим образом:
#
# d1 = render("123")   # 123 (целое число)
# d2 = render("45.54")   # None (не целое число)
# d3 = render("-56")   # -56 (целое число)
# d4 = render("12fg")  # None (не целое число)
# d5 = render("abc")   # None (не целое число)
# Декорируйте стандартную функцию input декоратором InputValues и объектом рендера класса RenderDigit так, чтобы на выходе при вводе целых чисел через пробел возвращался список из введенных значений. А на месте не целочисленных данных - значение None.
#
# Например, при вводе строки:
#
# "1 -5.3 0.34 abc 45f -5"
#
# должен возвращаться список:
#
# [1, None, None, None, None, -5]
#
# Назовите декорированную функцию input_dg и вызовите ее командой:
#
# res = input_dg()
#
# Создайте декоратор, который принимает список чисел и умножает результат функции на все элементы этого списка.
# class Multiply:
#     def __init__(self, nums_list):
#         self.nums_list = nums_list
#
#     def __call__(self, func):
#         def wrapper(num_multiply, *args, **kwargs):
#             resalt = func(*args, **kwargs)
#             return resalt * num_multiply
#         return wrapper
#
#     def __str__(self):
#        return f'{self.nums_list}'
#
# @Multiply
# def sum(a, b):
#     return a + b
#
# multiply = Multiply([4, 5, 6])
# print(multiply)
import time


# Создайте декоратор, который принимает параметр "retry_count" и повторяет выполнение функции
# заданное количество раз в случае возникновения исключения.
# class Repeater:
#     def __init__(self, number_repeat):
#         self.number_repeat = number_repeat
#
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             for _ in range(self.number_repeat):
#                 try:
#                     result = func(*args, **kwargs)
#                     return result
#                 except Exception as e:
#                     print(f"Error: {e}")
#             raise ValueError(f"Function {func.__name__} failed after {self.number_repeat} attempts.")
#         return wrapper
#
#     def __str__(self):
#         return f'{self.number_repeat}'
#
# @Repeater(3)
# def sum(a, b):
#     if a + b > 10:
#         raise ValueError("Sum is greater than 10")
#     return a + b
#
# repeater = Repeater(3)
# result = repeater(sum)(3, 5)
# print(result)