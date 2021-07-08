#!/usr/bin/python
# -*- coding: utf-8 -*-

#    https://www.youtube.com/watch?v=P0uvWDpqB8I&list=PLA0M1Bcd0w8zo9ND-7yEFjoHBg_fzaQ-B&index=17
#    17. ООП Python 3: коллекция __slots__ для классов
import timeit


class Point:
    """ в экземпляр класс можно добавить ещё координату """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calk(self):
        self.x += 1
        del self.y
        self.y = 0


pt1 = Point(1, 2)
pt1.z = 55
print(f"pt1.__dict__ {pt1.__dict__}")


class Point2d:
    """ в экземпляр класс нельзя  добавить ещё координату
        AttributeError: 'Point2d' object has no attribute 'z'
    """

    __slots__ = ("x", "y")
    MAX_CORDS = 100

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calk(self):
        self.x += 1
        del self.y
        self.y = 0


pt2 = Point2d(1, 2)
print(f"pt2.__dict__ {pt2.__slots__}")
print(f"pt2.x = {pt2.x}  pt2.y = {pt2.y}")
t1 = timeit.timeit(pt1.calk)
t2 = timeit.timeit(pt2.calk)
print(f"time pt1 {t1} time pt2 {t2}")
