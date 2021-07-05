#!/usr/bin/python
# -*- coding: utf-8 -*-

#   https://www.youtube.com/watch?v=bME7gXAM06c
#   Python 3 #21: функции map, filter, zip
a = [1, 2, 3, 4, 5, ]
b = [10, 20, 30, 40, 50]
d = "abracadabra"

c = zip(a, b)  # получение списка из кортежей
print(list(c))
c1 = zip(a, b, d)  # получение списка из кортежей
print(list(c1))
