# Объявите два класса:
# Cell - для представления клетки игрового поля;
# GamePole - для управления игровым полем, размером (N x N) клеток.
# С помощью класса Cell предполагается создавать отдельные клетки командой:
# c1 = Cell(around_mines, mine)
# Здесь around_mines - число мин вокруг данной клетки поля;
# mine - булева величина(True / False), означающая наличие мины
# в текущей клетке.\
# При этом, в каждом объекте класса Cell должны создаваться локальные свойства:
# around_mines - число мин вокруг клетки(начальное значение 0);
# mine - наличие / отсутствие мины в текущей клетке(True / False);
# fl_open - открыта / закрыта клетка - булево значение(True / False).\
# Изначально все клетки закрыты(False).
# С помощью класса GamePole должна быть возможность создавать квадратное
# игровое поле с
# числом клеток N x N:
# pole_game = GamePole(N, M)
# Здесь N - размер поля; M - общее число мин на поле.\
# При этом, каждая клетка представляется объектом класса Cell и все объекты
# хранятся в двумерном
# списке N x N элементов - локальном свойстве pole объекта класса GamePole.
# В классе GamePole должны быть также реализованы следующие методы:

# init() - инициализация поля с новой расстановкой M мин(случайным образом по
# игровому полю, # разумеется каждая мина должна находиться в отдельной клетке).
# show() - отображение поля в консоли в виде таблицы чисел открытых клеток
# (если клетка не открыта, то # отображается символ  # ;
# мина отображается символом *; между клетками при отображении ставить пробел).
# При создании экземпляра класса GamePole в его инициализаторе
# следует вызывать метод init()
# для первоначальной инициализации игрового поля. В классе GamePole
# могут быть и другие вспомогательные методы.
# Создайте экземпляр pole_game класса GamePole с размером поля N = 10 и
# числом мин M = 12.

import random


# _Cell__mine

class CellDescriptor:
    def __set_name__(self, owner, name):
        self.name = f'_{owner.__name__}__{name}'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        setattr(instance, self.name, value)


class Cell:
    mine = CellDescriptor()
    is_open = CellDescriptor()
    around_mines = CellDescriptor()

    def __init__(self, around_mines=0, mine=False):
        self.around_mines = around_mines
        self.mine = mine
        self.is_open = False


class GamePole:
    def __init__(self, size, mines):
        self.__size = size
        self.__mines = mines
        self.__pole = [[Cell() for _ in range(size)] for _ in range(size)]
        self.__initialize_pole()

    def __initialize_pole(self):
        total_mines = 0
        while total_mines < self.__mines:
            row, col = random.randint(0, self.__size - 1), random.randint(0, self.__size - 1)
            if not self.__pole[row][col].mine:
                self.__pole[row][col].mine = True
                total_mines += 1

    def show(self):
        for row in self.__pole:
            for cell in row:
                if cell.is_open:
                    if cell.mine:
                        print("*", end=" ")
                    else:
                        print(cell.around_mines, end=" ")
                else:
                    print('#', end=' ')
            print()


pole = GamePole(10, 12)
pole.show()
