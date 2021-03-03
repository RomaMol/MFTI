#!/usr/bin/python
# -*- coding: utf-8 -*-
#   https://www.youtube.com/watch?v=rZY9CJn1y2E&list=PLA0M1Bcd0w8zo9ND-7yEFjoHBg_fzaQ-B&index=13
#   ООП Python 3 #13: методы класса - @classmethod и статические методы - @staticmethod

class Vector:
    """существует класс Vector"""
    MIN_COORD = 0
    MAX_CORD = 100  # статичесике атрибуты == данные

    def setcoord(self, x, y):
        """атрибуты == данные получаемые после создания
        экземпляра класса и передоваемые экземпляру при вызове метода
        имеет доступ к атрибутам м методам всего класса и экземпляров класса
        """
        if Vector.validate(x) and Vector.validate(y):
            self.x = x
            self.y = y
            print(f"def setcoord self, x, y  self.x = {self.x}\n"
                  f"self.y = {self.y}")

    @classmethod
    def validate(cls, arg):
        """имеет доступ к атрибутам м методам только этого класса
        cls --- это имя класса  Vector
        """
        if arg >= cls.MIN_COORD and arg <= cls.MAX_CORD:
            return True
        return False

    @staticmethod
    def fun1(x, y):
        """Изолированый метод не связан с классом"""
        v2 = x * x + y * 2
        print(f"v2  {v2}")


v1 = Vector()
v1.setcoord(2, 4)
Vector.setcoord(v1, 20, 40)  # net @  --- добавляем экземпляр класса
Vector.validate(330)  # @classmethod
Vector.fun1(4, 6)  # @staticmethod
