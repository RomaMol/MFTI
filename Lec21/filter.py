#!/usr/bin/python
# -*- coding: utf-8 -*-

#   https://www.youtube.com/watch?v=bME7gXAM06c
#   Python 3 #21: функции map, filter, zip


def odd(x):
    return x % 2


lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a = filter(odd, lst)
print(a)
print(list(a))

b = filter(lambda x: x % 2, lst)
print(b)
print("list b нечетные числа ", list(b))
c = filter(lambda x: not x % 2, lst)
print("c", c)
print("list c четные числа", list(c))

lst1 = ["Москва", "Москва1", "Курск", "Курск1"]

d = filter(str.isalpha, lst1)
print("list d ", list(d))