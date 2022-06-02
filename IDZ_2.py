#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from math import pi, sqrt, cos, sin
from abc import ABC, abstractmethod


class Triangle(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def square(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def print_info(self):
        print("Base class method")
        print(f"The area of the triangle is: {self.square()}")
        print(f"The perimeter of the triangle is: {self.perimeter()}")


class RectTriangle(Triangle):
    def __init__(self, side1, side2, angle):
        self.__side1 = side1
        self.__side2 = side2
        self.__angle = angle * pi

    def square(self):
        return 0.5 * self.__side1 * self.__side2

    def perimeter(self):
        return self.__side1 + self.__side2 + \
               sqrt(self.__side1 ** 2 + self.__side2 ** 2 -
                    2 * self.__side1 * self.__side2 * cos(self.__angle))


class IsosTriangle(Triangle):
    def __init__(self, side1, side2, angle):
        self.__side1 = side1
        self.__side2 = side2
        self.__angle = angle * pi

    def square(self):
        return 0.5 * self.__side1 * self.__side2 * sin(self.__angle)

    def perimeter(self):
        return self.__side1 + self.__side2 + \
               sqrt(self.__side1 ** 2 + self.__side2 ** 2 -
                    2 * self.__side1 * self.__side2 * cos(self.__angle))


class EquilTriangle(Triangle):
    def __init__(self, side1, side2, angle):
        if side1 != side2 or angle != 60:
            raise ValueError
        else:
            self.__side1 = side1
            self.__side2 = side2
            self.__angle = angle * pi

    def square(self):
        return (sqrt(3.0) / 4) * self.__side1 ** 2

    def perimeter(self):
        return 3 * self.__side1


if __name__ == '__main__':
    rt = RectTriangle(3, 5, 30)
    print(f"Area of the Rect Triangle is: {rt.square()}")
    print(f"Perimeter of the Rect Triangle is: {rt.perimeter()}")
    it = IsosTriangle(4, 4, 67)
    print(f"Area of the Isosceles Triangle is: {it.square()}")
    print(f"Perimeter of the Isosceles Triangle is: {it.perimeter()}")
    et = EquilTriangle(10, 10, 60)
    print(f"Area of the Equilateral Triangle is: {et.square()}")
    print(f"Perimeter of the Equilateral Triangle is: {et.perimeter()}")
    rt.print_info()
    it.print_info()
    et.print_info()



