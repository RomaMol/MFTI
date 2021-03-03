#!/usr/bin/python
# -*- coding: utf-8 -*-
#   https://www.youtube.com/watch?v=KlW6O-5pcuU&list=PLA0M1Bcd0w8zo9ND-7yEFjoHBg_fzaQ-B&index=12
#   ООП Python 3 #12: нейронная сеть (пример реализации)
import random

import self as self

from Lec12.link import Link
from Lec12.nero import Nero


class NetWork:

    def __init__(self, *args):
        """аргументы в числе слоев NetWork(10, 5, 3)
        10-5-5 аргументы в 3 слоях
        """
        self.__nlayer = len(args)  # число слоев
        self.__neuros = args  # список число нейронов в слое
        self.__layers = []   #  список нейронов в каждом слое
        print(f" *args = {args}")

        # Создаем нейроны для каждого слоя
        for i in range(self.__nlayer):
            self.__layers.append([Nero([], []) for n in range(self.__neuros[i])])
            print(self.__layers)

        # создаем связи между нейронами
        for i in range(self.__nlayer):
            for neuro in self.__layers[i]:  # перебираем нейроны i-го слоя
                list_in = 0 if i == 0 else [Link(n_in, neuro, random.random()) for n_in in self.__layers[i - 1]]
                list_out = 0 if i == self.__nlayer - 1 else [Link(neuro, n_out, random.random()) for n_out in
                                                             self.__layers[i + 1]]
                neuro.list_in = list_in
                neuro.list_out = list_out

    def run(self, v=None):
        # подаем на вход нейронов сигнал v
        for neuro, inp in zip(self.__layers[0], v):
            neuro.value = neuro.list_in = inp

        # проводим сигнал по нейронной сети
        for i in range(1, self.__nlayer):
            for neuro in self.__layers[i]:  # перебираем нейроны i-го слоя
                v = [(link.n_in.value * link.w) for link in neuro.list_in] # v = (входной нейрон * вес связи)
                print(f"v {v}", sep="\n")
                neuro.value = neuro.act(sum(v))  #  act(v) = 1 / (1 + math.exp(-v))

    def output(self):
        return [neuro.value for neuro in self.__layers[-1]]
