# давайте рассмотрим ещё одну задачу.
# Создайте класс Power, который будет представлять функцию степени.
# Этот класс должен иметь метод __call__,
# который принимает число x и возвращает его
# значение, возведенное в степень n.

# class Power:
#     def __init__(self, number):
#         self.number = number
#
#     def __setattr__(self, key, value):
#         if key == 'number':
#             if not isinstance(value, (int, float)):
#                 raise ValueError('неверно указаны исходные данные')
#         object.__setattr__(self, key, value)
#
#     def __str__(self):
#         return f'{self.number} '
#
#     def __call__(self, number_degree, *args, **kwargs):
#         return self.number ** number_degree
#
# power_function = Power(3)
# result = power_function(2)
# print(result)
