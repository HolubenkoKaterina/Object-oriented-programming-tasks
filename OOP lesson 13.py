# Вам требуется сформировать класс PathLines для описания маршрутов, состоящих из линейных сегментов.
# При этом каждый линейный сегмент предполагается задавать отдельным классом LineTo.
# Объекты этого класса будут формироваться командой:
# line = LineTo(x, y)
# где x, y - следующая координата линейного участка (начало маршрута из точки 0, 0).
# В каждом объекте класса LineTo должны формироваться локальные атрибуты:
# x, y - для хранения координат конца линии (начало определяется по координатам предыдущего объекта).
# Объекты класса PathLines должны создаваться командами:
# p = PathLines()                   # начало маршрута из точки 0, 0
# p = PathLines(line1, line2, ...)  # начало маршрута из точки 0, 0
# где line1, line2, ... - объекты класса LineTo.
# Сам же класс PathLines должен иметь следующие методы:
# get_path() - возвращает список из объектов класса LineTo (если объектов нет, то пустой список);
# get_length() - возвращает суммарную длину пути (сумма длин всех линейных сегментов);
# add_line(self, line) - добавление нового линейного сегмента (объекта класса LineTo) в конец маршрута.
# Пояснение: суммарный маршрут - это сумма длин всех линейных сегментов,
# а длина каждого линейного сегмента определяется как евклидовое расстояние по формуле:
# L = sqrt((x1-x0)^2 + (y1-y0)^2)
# где x0, y0 - предыдущая точка маршрута; x1, y1 - текущая точка маршрута.
# Пример использования классов (эти строчки в программе писать не нужно):
# p = PathLines(LineTo(10, 20), LineTo(10, 30))
# p.add_line(LineTo(20, -10))
# dist = p.get_length()
import math


class PathLines:
    def __init__(self, *lines):  # (lineTo1, lineTo2)
        self.__path_lines = list(lines)

    @property
    def path_lines(self):
        return self.__path_lines.copy()

    def get_length(self):
        total_length = 0
        for index in range(1, len(self.__path_lines)):
            x0, y0 = self.__path_lines[index - 1].x, self.__path_lines[index - 1].y
            x1, y1 = self.__path_lines[index].x, self.__path_lines[index].y
            total_length += math.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)
        return total_length

    def add_line(self, line):
        # if not self.path_lines:
        self.__path_lines.append(line)
        # else:
        #     x0, y0 = self.path_lines[-1].x, self.path_lines[-1].y
        #     x1, y1 = line.x, line.y
        #     length = math.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)

class LineTo:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        # self.start_x = 0
        # self.start_y = 0


lineTo1 = LineTo(2, 4)
lineTo2 = LineTo(12, 14)
p1 = PathLines(lineTo1, lineTo2)
# p1 = [lineTo1, lineTo2]  # [[2, 4], [12, 14]]
print(p1.get_length())
p1.add_line(LineTo(22, 34))
print(p1.get_length())