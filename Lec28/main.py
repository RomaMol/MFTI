#!/usr/bin/python
# -*- coding: utf-8 -*-

#   https://www.youtube.com/watch?v=TdeZKWBppo4
#   Python 3 #28: декораторы функций и замыкания
import time


def getnod(aa, bb):
    """Реализация функции поиск наименьший общий делитель"""

    while aa != bb:
        if aa > bb:
            aa -= bb
        else:
            bb -= aa
    print(f"getnod a = {aa}")
    return aa


def getfastnod(aa, bb):
    """быстрый алгоритм евклида для поиска НОД"""
    if aa < bb:
        aa, bb = bb, aa
    while bb:
        aa, bb = bb, aa % bb

    print(f"getfastnod a = {aa}")
    return aa


def testtime(fn):
    """Функция декаратор
    Функция проверки времени выполнения функции getnod   """

    def wraper(*args, **kwargs):
        """Функция обертка в которой происходит вычисление"""
        st = time.time()
        fn(*args, **kwargs)
        delta = time.time() - st
        print(f'время работы функции "fn" = {delta} сек')

    return wraper


# a = 10
# b = 12
# nod = getnod(a, b)
# print(f'a = {a}, b ={b}, поиск наименьший общий делитель nod = {nod}')

test1 = testtime(getnod)
test2 = testtime(getfastnod)
test1(10000000, 4356464)
test2(1000000000000000, 4356464)

