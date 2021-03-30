#!/usr/bin/python
# -*- coding: utf-8 -*-

#   https://www.youtube.com/watch?v=gMM7632kTkI
#   Python 3 #11: списки - инструмент list comprehensions, сортировка методом выбора

n= 11
a = list(range(n))
print(f'n= {n}          a = {a}')

for i in range(n//2):
    a[i], a[n-i-1] = a[n-i-1],a[i]

print(f'n= {n}  reverse a = {a}')