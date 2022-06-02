#Вариант №12
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


class Number:
    def __init__(self, num):
        self.__num = float(num)

    def change_num(self, new_num):
        self.__num = float(new_num)

    def print_info(self):
        print("Class Number")
        print(f"Num: {self.__num}")

    def add(self, rhs):
        return self.__num + rhs

    def div(self, rhs):
        rhs = float(rhs)
        return self.__num // rhs


class Real(Number):
    def __init__(self, num):
        super().__init__(num)

    def step(self, rhs):
        return self.__num ** rhs

    def logs(self, rhs):
        return math.log(self.__num, rhs)


if __name__ == '__main__':
    numb = Number(5.0)
    numb.print_info()
    numb.change_num(10.0)
    numb.print_info()
    st1 = 10.0
    st2 = numb.add(st1)
    st3 = st2.div(st1)
    st4 = Real(15.2)
    st4.change_num(16.1)
    st4.print_info()
    st5 = st4.step(2)
    st6 = st4.logs(2)

