#!/usr/bin/python
# -*- coding: utf-8 -*-

#    https://www.youtube.com/watch?v=F7KxC6JTmsc&list=PLA0M1Bcd0w8zo9ND-7yEFjoHBg_fzaQ-B&index=16

#    16. ООП Python 3: магические методы __str__, __repr__, __len__, __abs__

#    __str__(self) - вызывается функциями str, print  и  format.Возвращает строковое представление объекта.
#    __len__(self) - длина объекта. Функция len() возвращает длину (количество элементов) в объекте.
#    __abs__(self) - модуль (abs()).
#       abs() — это встроенная функция, возвращающая абсолютное значение числа

class Cat:
    """Класс Кошки """

    def __init__(self, name):
        """Класс Кошки при создании класса передаем имя кошки """
        self.name = name

    def __repr__(self):  # переопределение метода
        """ до переопределения  <__main__.Cat object at 0x000001C32FB78FA0>
            после переопределения  <class '__main__.Cat'>: vasia
        """
        return f"{self.__class__}: {self.name}"

#    __str__(self) - вызывается функциями str, print  и  format.Возвращает строковое представление объекта.

    def __str__(self):
        """ до переопределения  <__main__.Cat object at 0x000001C32FB78FA0>
        __init__(self, name): -->  self.name = name
            после переопределения  vasia
        """
        return f"{self.name}"



cat1 = Cat("vasia")
print(cat1.__str__())
print(cat1.__repr__())



class Point:
    """Класс точка с координатами в плоскости  Х У """

    def __init__(self, *args):
        self.__coords = args

    def __len__(self):
        """ до переопределения  TypeError: object of type 'Point' has no len()
            после переопределения  2 --> XY and 3 --> XYZ
        """
        return len(self.__coords)

    def __abs__(self):
        """ до переопределения  TypeError: bad operand type for abs(): 'Point'
            после переопределения  [12, 342, 34]
        """
        return list(map(abs, self.__coords))


p = Point(-12, 342,-34)
print(len(p))
print(abs(p))
