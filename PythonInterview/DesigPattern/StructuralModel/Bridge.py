"""
桥接模式
"""
from abc import ABC, abstractmethod


class Color():
    def __init__(self, color):
        self._color = color


class Shape(ABC):
    color = None

    def __init__(self, shape: str) -> None:
        self._shape = shape

    def setColor(self, color: Color) -> None:
        self.color = color
    def msg(self):
        print(f'shape:{self._shape},color{self.color._color}')

class Circle(Shape):
    pass

class Square(Shape):
    pass


if __name__ == "__main__":
    red = Color('Red')
    blue = Color('Blue')

    c1 = Circle('circle')
    c1.setColor(red)
    c1.msg()

    c2 = Circle('circle')
    c2.setColor(blue)
    c2.msg()

    s1 = Square('square')
    s1.setColor(red)
    s1.msg()

    s2 = Square('square')
    s2.setColor(blue)
    s2.msg()
