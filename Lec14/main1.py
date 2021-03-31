#!/usr/bin/python
# -*- coding: utf-8 -*-

#   https://www.youtube.com/watch?v=WElr9nSS6bo
#   Python 3 #14: функции (def) - объявление и вызов

def perandsq(w, h):
    return 2 * (w + h), w * h


print(perandsq(4, 8))
per, sq = perandsq(3, 5)
print(f'per = {per}, sq = {sq}')


def max2(a, b):
    if a > b:
        return a
    else:
        return b


def max3(a, b, c):
    return max2(a, max2(b, c))

print(" dano: ",(3, 7, 5))
print(" max = ",max3(3, 7, 5))
