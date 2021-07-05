#!/usr/bin/python
# -*- coding: utf-8 -*-

#    https://www.youtube.com/watch?v=F7KxC6JTmsc&list=PLA0M1Bcd0w8zo9ND-7yEFjoHBg_fzaQ-B&index=16

#    16. ООП Python 3: магические методы __str__, __repr__, __len__, __abs__

class Cat:
    """Класс Кошки """

    def __init__(self, name):
        """Класс Кошки при создании класса передаем имя кошки """
        self.name = name


cat1  =  Cat("vasia")
print(cat1.__str__())
print(cat1.__repr__())
#print(cat1.__len__())
print(cat1.__class__)
