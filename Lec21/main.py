#!/usr/bin/python
# -*- coding: utf-8 -*-

#   https://www.youtube.com/watch?v=bME7gXAM06c
#   Python 3 #21: функции map, filter, zip

lst = (x for x in range(11))


def sql(x):
    return x ** 2


b = map(sql, lst)
c = (sql(x) for x in range(11))
print(list(b))
print(list(c))

lst = ("Москва", "Орел","Курск")
d = map(str.upper, lst)
print(list(d))