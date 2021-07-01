#!/usr/bin/python
# -*- coding: utf-8 -*-
import time


def testtime(fn):
    """Функция декаратор
    Функция проверки времени выполнения функции getnod """

    def wraper(*args, **kwargs):
        """Функция обертка в которой происходит вычисление"""
        st = time.time()
        res = fn(*args, **kwargs)
        delta = time.time() - st
        print(f'время работы функции "fn" = {delta} сек')
        return res

    return wraper


@testtime
def spisoknadva(n):
    """функция создания списка четных чисел от 0 до Н введенного числа"""
    testlist = []
    x = 0
    while x < n:
        testlist.append(x)
        x = x + 2
    return testlist


@testtime
def spisoknadva2(input_n):
    """функция создания списка четных чисел от 0 до Н введенного числа   list comprehension"""
    spisok_do_n = [input_n for input_n in range(0, input_n)]

    testlist2 = [item for item in spisok_do_n if item % 2 == 0]

    return testlist2


n = int(input("Введите число :"))
spisoknadva(n)
spisoknadva2(n)
#print(f'списка четных чисел от 0 до введенного числа {spisoknadva(n)}')
#print(f'списка четных чисел от 0 до введенного числа {spisoknadva2(n)}')
