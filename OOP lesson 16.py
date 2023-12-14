# Объявите в программе класс WindowDlg, объекты которого предполагается создавать командой:
# wnd = WindowDlg(заголовок окна, ширина, высота)
# В каждом объекте класса WindowDlg должны создаваться приватные локальные атрибуты:
# __title - заголовок окна (строка);
# __width, __height - ширина и высота окна (числа).
# В классе WindowDlg необходимо реализовать метод:
# show() - для отображения окна на экране (выводит в консоль строку в формате:
# "<Заголовок>: <ширина>, <высота>", например "Диалог 1: 100, 50").
# Также в классе WindowDlg необходимо реализовать два объекта-свойства:
# width - для изменения и считывания ширины окна;
# height - для изменения и считывания высоты окна.
# При изменении размеров окна необходимо выполнять проверку:
# - переданное значение является целым числом в диапазоне [0; 10000].
# Если хотя бы один размер изменился (высота или ширина),
# то следует выполнить автоматическую перерисовку окна (вызвать метод show()).
# При начальной инициализации размеров width, height вызывать метод show() не нужно.

class WindowDlg:
    VALUE_START = 0
    VALUE_FINISH = 10000

    def __init__(self, title, width, height):
        self.__title = title
        self.width = width
        self.__hight = height

    def change_width(self, width):
      if self.check_value(width) == True:
          self.__width = width

    def change_height(self, height):
      if self.check_value(height) == True:
          self.__height = height
          self.show()

    @classmethod
    def check_value(cls, value):
        if WindowDlg.VALUE_START <= value >= WindowDlg.VALUE_FINISH == True:
            return value
        else:
            raise 'диапазон недопустимый!'

    def show(self):
        return f'{self.__title}: {self.width}, {self.__hight}'

wnd_11 = WindowDlg('window 11', 50, 150)
print(wnd_11.show())
wnd_21 = WindowDlg('window 21', 100, 150)
print(wnd_21.show())
print(wnd_21.change_height(10000000))

