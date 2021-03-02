#!/usr/bin/python
# -*- coding: utf-8 -*-
#   https://www.youtube.com/watch?v=KlW6O-5pcuU&list=PLA0M1Bcd0w8zo9ND-7yEFjoHBg_fzaQ-B&index=12
#   ООП Python 3 #12: нейронная сеть (пример реализации)



class Link:
    """Описание одной связи межде нейронами"""

    def __init__(self, n_in, n_out, w=0):
        """конструктор
        n_in - входной нейрон  n_out  - выходной нейрон
        сохраняем в локальных свойствах  self.__in self.__out
        self.__w = 0 - значение или вес связи 
                """
        self.__in = n_in
        self.__out = n_out
        self.__w = w

    @property
    def n_in(self):
        """возвращает свойства входных связей"""
        return self.__in

    @property
    def n_out(self):
        """возвращает свойства входных связей"""
        return self.__out

    @property
    def w(self):
        """возвращает свойства входных связей"""
        return self.__w