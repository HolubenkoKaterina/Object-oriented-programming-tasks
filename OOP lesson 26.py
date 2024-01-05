# Создайте класс Rectangle, представляющий прямоугольник. У прямоугольника должны быть атрибуты width (ширина) и height (высота). Реализуйте сеттеры для этих атрибутов таким образом, чтобы выполнялись следующие условия:
# Ширина и высота должны быть положительными числами.
# После установки новой ширины или высоты прямоугольника, пересчитывайте его площадь и обновляйте атрибут area.
# Используйте эти условия для написания сеттеров.

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not (isinstance(value, int) and value > 0):
            raise ValueError('Ширина должна быть положительным числом')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not (isinstance(value, int) and value > 0):
            raise ValueError('Высота должна быть положительным числом')
        self.__height = value

    @property
    def area(self):
        return self.__height * self.__width

    def __str__(self):
        return f'Ширина: {self.__width}, Высота: {self.__height}, Площадь: {self.area}'


rect = Rectangle(-5, 5)
print(rect)
