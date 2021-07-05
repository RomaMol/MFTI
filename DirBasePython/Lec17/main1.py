#!/usr/bin/python
# -*- coding: utf-8 -*-

#   https://www.youtube.com/watch?v=8HvcVQWR2gY
#   Python 3 #17: алгоритм Евклида (НОД), принцип тестирования программ
import time


def getnod(a, b):
    """ Программа поиска наименьшего общего делителя НОД
    """
    if a < b:
        a, b = b, a

    while b > 0:
        a, b = b, a % b
        # t = b
        # b = a % b
        # a = t
    return a


def testnod():
    """ тестирование метода по изветным данным"""
    # ---test1 - ---------------------------------------------------
    a = 18
    b = 24
    res = getnod(a, b)
    if res == 6:
        print("test-1 OK")
    else:
        print("test-1 FAILED")

    # ---test2 - ---------------------------------------------------
    a = 100
    b = 1
    res = getnod(a, b)
    if res == 1:
        print("test-2 OK")
    else:
        print("test-2 FAILED")

    # ---test3 - ---------------------------------------------------
    a = 1000000000000
    b = 9785
    st = time.time()
    res = getnod(a, b)
    et = time.time()
    tt = et - st
    if res == 5 and tt < 1:
        print("test-3 OK", "time=", tt, "NOD =", res)
    else:
        print("test-3 FAILED", "time=", tt, "NOD =", res)


print(getnod(18, 24))
testnod()
