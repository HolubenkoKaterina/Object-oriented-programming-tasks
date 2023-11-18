# # Объявите в программе класс Cart (корзина), объекты которого создаются командой:
# # cart = Cart()
# # Каждый объект класса Cart должен иметь локальное свойство
# # goods - список объектов для покупки (объекты классов Table, TV, Notebook и Cup).
# # Изначально этот список должен быть пустым.
#
# # В классе Cart объявить методы:
# # add(self, gd) - добавление в корзину товара, представленного объектом gd;
# # remove(self, indx) - удаление из корзины товара по индексу indx;
# # get_list(self) - получение из корзины товаров в виде списка из строк:
# # ['<наименовние_1>: <цена_1>',
# # '<наименовние_2>: <цена_2>',
# # '<наименовние_N>: <цена_N>']
#
# # Объявите в программе следующие классы для описания товаров:
# # Table - столы;
# # TV - телевизоры;
# # Notebook - ноутбуки;
# # Cup - кружки.
#
# # Объекты этих классов должны создаваться командой:
# # gd = ИмяКласса(name, price)
# # Каждый объект классов товаров должен содержать локальные свойства:
# # name - наименование;
# # price - цена.
# # Создайте в программе объект cart класса Cart.
# # Добавьте в него два телевизора (TV), один стол (Table), два ноутбука (Notebook) и одну кружку (Cup). Названия и цены придумайте сами.
# class Cart:
#     def __init__(self):
#         self.goods = []
#
#     def add(self, gd):
#         self.goods.append(gd)
#
#     def remove(self, indx):
#         del self.goods[indx]
#
#     def get_list(self):
#         return [f'{elem.name}: {elem.price}' for elem in self.goods]
#
# class Table:
#
#     def __init__(self, name,price):
#         self.price = price
#         self.name = name
#
#
# class TV:
#
#     def __init__(self, name, price):
#         self.price = price
#         self.name = name
#
# class Notebook:
#
#     def __init__(self, name, price):
#         self.price = price
#         self.name = name
#
# class Cup:
#
#     def __init__(self, name, price):
#         self.price = price
#         self.name = name
#
#
#
# table1 = Table('Стол письменный', 500)
# tv1 = TV('Телевизор Samsung', 1000)
# notebook1 = Notebook('Ноутбук Dell', 800)
# cup1 = Cup('Кружка с логотипом', 10)
#
# cart = Cart()
# cart.add(table1)
# cart.add(tv1)
# cart.add(notebook1)
# cart.add(cup1)
#
# print("Товары в корзине:")
# for idx, elem in enumerate(cart.get_list()):
#     print(f'{idx + 1}. {elem}')
#
# # Удалим стол из корзины
# cart.remove(0)
#
# print("\nТовары в корзине после удаления стола:")
# for idx, elem in enumerate(cart.get_list()):
#     print(f'{idx + 1}. {elem}')
