#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Table:
    def __init__(self, l, w, h):
        self.length = l
        self.width = w
        self.height = h


class DeskTable(Table):
    def square(self):
        return self.width * self.length


if __name__ == '__main__':
    t1 = Table(1.5, 1.8, 0.75)
    t2 = DeskTable(0.8, 0.6, 0.7)
    print(t2.square())

class Rectangle(Figure):
    def __init__(self, width, height, color):
        super().__init__(color)
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, w):
        if w > 0:
            self.__width = w
        else:
            raise ValueError

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, h):
        if h > 0:
            self.__height = h
        else:
            raise ValueError

    def area(self):
        return self.__width * self.__height

    def info(self):
        print("Rectangle")
        print("Color: " + self.color)
        print("Width: " + str(self.width))
        print("Height: " + str(self.height))
        print("Area: " + str(self.area()))


if __name__ == '__main__':
    fig = Figure("orange")
    fig.info()
    rect = Rectangle(10, 20, "green")
    rect.info()
