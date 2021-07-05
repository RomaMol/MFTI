#!/usr/bin/python
# -*- coding: utf-8 -*-

#    https://www.youtube.com/watch?v=9qr3neFX0Rs&list=PLA0M1Bcd0w8zo9ND-7yEFjoHBg_fzaQ-B&index=14

#    ООП Python 3 #14: полиморфизм в ООП на Python

""" getPerimetr - имя метода одинаковое для разных классов со схожим вычислением """


class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.name = "Rectangle Perimetr"

    def getPerRect(self):
        return 2 * (self.w + self.h)

    def getPerimetr(self):
        return 2 * (self.w + self.h)


class Square:
    def __init__(self, a):
        self.a = a
        self.name = "Square Perimetr"

    def getPerSq(self):
        return 4 * self.a

    def getPerimetr(self):
        return  4 * self.a


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.name = "Triangle Perimetr"

    def getPerTr(self):
        return self.a + self.b + self.c

    def getPerimetr(self):
        return  self.a + self.b + self.c


r1 = Rectangle(1, 2)
r2 = Rectangle(3, 4)
s1 = Square(10)
s2 = Square(20)
t1 = Triangle(1, 2, 3)
t2 = Triangle(4, 5, 6)

geom = [r1, r2, s1, s2, t1, t2]

for g in geom:
    print(f'{g.name} = {g.getPerimetr()}')
