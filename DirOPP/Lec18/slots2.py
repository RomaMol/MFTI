#!/usr/bin/python
# -*- coding: utf-8 -*-

#    https://www.youtube.com/watch?v=xPsyicLd89g&list=PLA0M1Bcd0w8zo9ND-7yEFjoHBg_fzaQ-B&index=18
#    18. ООП Python 3: как работает __slots__ с property и при наследовании классов
import math


class Point2d:
    """ в экземпляр класс нельзя  добавить ещё координату
        AttributeError: 'Point2d' object has no attribute 'z'
    """

    __slots__ = ("x", "y", "__lends")
    MAX_CORDS = 100

    def __init__(self, x, y):
        """инициализация- описание переменных используемых классом"""
        self.x = x
        self.y = y
        self.lends = math.sqrt(x * x + y * y)

    @property
    def lends(self):
        return self.__lends

    @lends.setter
    def lends(self, value):
        self.__lends = value


pt = Point2d(2, 7)
print(f' lends = {pt.lends}, x = {pt.x}, y = {pt.y}')


class Point3d(Point2d):
    """Новый класс наследуется от класса class Point2d"""
    #__slots__ = "z"

    def __init__(self, x, y, z):
        """инициализация- описание переменных используемых классом"""
        super().__init__(x, y)  # взять переменные из базового класса
        self.z = z


pt3 = Point3d
pt3.z = 3
print(f"pt3.__dict__ = {pt3.__dict__}, pt3.__slots__= {pt3.__slots__}")
pt4 = Point3d(10,20,30)
print(f"pt4.x = {pt4.x}, pt4.y= {pt4.y}, pt4.z= {pt4.z}")