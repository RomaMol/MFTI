#!/usr/bin/python
# -*- coding: utf-8 -*-

#   https://www.youtube.com/watch?v=bME7gXAM06c
#   Python 3 #21: функции map, filter, zip

# map(функция, итерируемый объект(список))

lst = (x for x in range(11))


def sql(x):
    return x ** 2


b = map(sql, lst)
c = (sql(x) for x in range(11))
print(list(b))
print(list(c))

lst = ("Москва", "Орел", "Курск")
d = map(str.upper, lst)
print(list(d))

lst1 = ("Москва", "Орал", "Карск")
a = map(lambda x: x.replace('a', 'A'), lst1)
g = list(a)
print(g)

lst2 = ("Москва", "Орел", "Курск")
a = map(str.upper, lst2)
h = map(sorted, a)
print(list(h))

input_data = list(map(int,input("введите число :").split()))
print(input_data)