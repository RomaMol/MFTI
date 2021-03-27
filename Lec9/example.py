#!/usr/bin/python
# -*- coding: utf-8 -*-

#   https://www.youtube.com/watch?v=ImWIDeW4GH0
#   Python 3 #9: списки list и функции len, min, max, sum, sorted


lst = [-1, 0, 5, 3, 2]
print(f'lst {lst}')
for x in range(5):
    print(f'x = {x}, lst[x] = {lst[x]},   lst[x]*7.2 = {lst[x] * 7.2} ')
print(lst)
print()

for x in range(len(lst)):
    lst[x] = lst[x] * 7.2
    print(f'x = {x}, lst[x]*7.2 = {lst[x]}')
print(lst)
print()
nlst = []
for x in lst:
    x = int(x / 7.2)
    print(f'x = {x}')
    nlst.append(x)
print(f'lst {lst}')
print(f'nlst {nlst}')
