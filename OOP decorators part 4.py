# Напишите декоратор, который принимает параметр "delay" и задерживает выполнение функции на указанное количество секунд.
# class Delay:
#     def __init__(self, delay):
#         if isinstance(delay, int):
#             self.delay = delay
#         else:
#             raise ValueError
#
#     def __str__(self):
#         return f'время задержки выполнения функции: {self.delay}'
#
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             time.sleep(self.delay)
#             return func(*args, **kwargs)
#         return wrapper
#
# @Delay(4)
# def sum(a, b): return a + b
#
# delay = Delay(4)
# print(delay(sum)(2, 3))

# Создайте декоратор, который принимает параметр "n" и выполняет функцию "n" раз.
# class Repeat:
#     def __init__(self, n_repeat):
#         self.n_repeat = n_repeat
#
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             result = func(*args, **kwargs)
#             for _ in range(self.n_repeat):
#                 print(result)
#         return wrapper
#
#     def __str__(self):
#         return f'{self.n_repeat}'
#
# @Repeat(4)
# def text_return(text):
#     return text.upper()
#
# repeat = Repeat(4)
# repeat(text_return)('i like python')

# Напишите декоратор, который принимает параметр "message" и выводит это сообщение перед выполнением функции.
# class Message:
#     def __init__(self, text):
#         self.text = text
#
#     def __call__(self, func):
#         def wrapper(*args, **kwargs):
#             print(self.text)
#             resalt = func(*args, **kwargs)
#             return resalt
#         return wrapper
#
#     def __str__(self):
#         return f'{self.text}'
#
#
#
# @Message('very much!')
# def text_return(text):
#     return text.upper()
#
# result = text_return('i like python')
# print(result)