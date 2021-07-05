#!/usr/bin/python
# -*- coding: utf-8 -*-

#   https://www.youtube.com/watch?v=z6b_F3OC39s
#   Python 3 #16: рекурсивные и лямбда-функции, функции с произвольным числом аргументов

def pow(x, n):
    if n == 0:
        return 1
    else:
        return x * pow(x, n - 1)


step = pow(3, 5)

print(step)

a, b = (1, 2)
x, *y = (1, 2, 3, 4, 5, 6, 7)
print(f'a,b  = {a, b},  x,*y = {x, y}')

a = (-5, 6)
for x in range(*a):
    print(x, end=" ")
print()


def myfanc(*args):
    print('myfanc(*args)', args)


myfanc()
myfanc(x)
myfanc(1, 3, 5)
myfanc("x", 5, "eee")
