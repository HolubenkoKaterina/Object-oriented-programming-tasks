# class FloatValue:
#     def __get__(self, instance, owner):
#         return instance._value
#
#     def __set__(self, instance, value):
#         if not isinstance(value, float):
#             raise TypeError("Присваивать можно только вещественный тип данных.")
#         instance._value = value
#
#
# class Cell:
#     value = FloatValue()
#
#     def __init__(self):
#         self.value = 0.0
#
#
# class TableSheet:
#     def __init__(self, rows, columns):
#         self.columns = columns
#         self.rows = rows
#         self.cells = self.create_tablesheet()
#
#     def create_tablesheet(self):
#         cells = []
#         for i in range(self.columns):
#             row = [Cell() for _ in range(self.rows)]
#             cells.append(row)
#         return cells
#
#     def fill_table(self):
#         value = 1.0
#         for i in range(self.columns):
#             for j in range(self.rows):
#                 self.cells[i][j].value = value
#                 value += 1.0
#
#     def display_table(self):
#         for row in self.cells:
#             for cell in row:
#                 print(f"{cell.value:.2f}", end="\t")
#             print()
# # Создаем объект table класса TableSheet с размером таблицы N = 5, M = 3.
# table = TableSheet(rows=5, columns=3)
# # Заполняем таблицу числами от 1.0 до 15.0
# table.fill_table()
# table.display_table()
#
