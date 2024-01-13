# Задача: Магазин продуктов с использованием __call__
# Создайте класс Product, представляющий продукт в магазине.
# У продукта должны быть следующие атрибуты:
# name: название продукта (строка).
# price: цена продукта (вещественное число).
# stock: количество продукта в наличии (целое число).
# Реализуйте метод __call__(quantity), который будет уменьшать
# количество продукта в наличии на указанное количество (quantity).
# При этом необходимо учесть, что количество продукта в наличии не может стать отрицательным.

# class Product:
#     def __init__(self, name, price, stock):
#         self.name = name
#         self.price = price
#         self.stock = stock
#
#     def __setattr__(self, key, value):
#         if key == 'name':
#             if not isinstance(value, str):
#                 raise ValueError('название товара неверное')
#         elif key == 'price':
#             if not isinstance(value, (int, float)) or value < 0:
#                 raise ValueError('цена неверна')
#         elif key == 'stock':
#             if not isinstance(value, int) or value < 0:
#                 raise ValueError('остаток товара неверен')
#         object.__setattr__(self, key, value)
#
#     def __call__(self, quantity, *args, **kwargs):
#         if self.stock - quantity >= 0:
#             self.stock -= quantity
#             return self.stock
#         else:
#             raise ValueError('остаток товара меньше указанного количества')
#
#     def __str__(self):
#         return f'{self.stock} {self.name}'
#
# product = Product('tv', 10000, 50)
# product(5)
# print(product.stock)
# print(product.__dict__)

