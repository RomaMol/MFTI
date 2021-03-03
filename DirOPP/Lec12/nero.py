#!/usr/bin/python
# -*- coding: utf-8 -*-
#   https://www.youtube.com/watch?v=KlW6O-5pcuU&list=PLA0M1Bcd0w8zo9ND-7yEFjoHBg_fzaQ-B&index=12
#   ООП Python 3 #12: нейронная сеть (пример реализации)

import math


class Nero:
    """описание класса одного нейрона"""

    def __init__(self, list_in, list_out):
        """конструктор
        list_in -  список входных связей  list_out  -список выходных  связей
        сохраняем в локальных свойствах  self.__in self.__out
        self.__value = 0 - какое выходное значение имеет нейрон
        """

        self.__in = list_in  # список входных связей
        self.__out = list_out  # список выходных  связей
        self.__value = 0  # выходной сигнал с нейрона

    @property
    def list_in(self):
        """возвращает свойства входных связей"""
        return self.__in

    @list_in.setter
    def list_in(self, lst):
        """возвращает свойства входных связей"""
        self.__in = lst

    @property
    def list_out(self):
        """возвращает свойства выходных  связей"""
        return self.__out

    @list_out.setter
    def list_out(self, lst):
        """возвращает свойства выходных  связей"""
        self.__out = lst

    def act(self, x):
        """функция расчета значения взвешенного входного Х """
        return 1 / (1 + math.exp(-x))
