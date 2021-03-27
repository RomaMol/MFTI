#!/usr/bin/python
# -*- coding: utf-8 -*-

#   https://www.youtube.com/watch?v=ImWIDeW4GH0
#   Python 3 #9: списки list и функции len, min, max, sum, sorted


lst = ['Москва', "Питер", "Курск","Орел"]
print(f'lst : {lst}')
print(f'type(lst) : {type(lst)}')
print(f'lst[1] : {lst[1]}')
print(f'число элементов в списке с 1 len(lst) : {len(lst)}')
print(f'последний элемент в списке с 0 lst[len(lst)-1] : {lst[len(lst)-1]}')
print(f'или lst[-1] : {lst[-1]}')
for city in lst:
    print(city, type(city))