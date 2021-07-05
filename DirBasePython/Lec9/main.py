#!/usr/bin/python
# -*- coding: utf-8 -*-

#   https://www.youtube.com/watch?v=ImWIDeW4GH0
#   Python 3 #9: списки list и функции len, min, max, sum, sorted


lst = ['Москва', "Питер", "Курск", "Орел"]
print(f'lst : {lst}')
print(f'type(lst) : {type(lst)}')
print(f'lst[1] : {lst[1]}')
print(f'число элементов в списке с 1 len(lst) : {len(lst)}')
print(f'последний элемент в списке с 0 lst[len(lst)-1] : {lst[len(lst) - 1]}')
print(f'или lst[-1] : {lst[-1]}')
for city in lst:
    print(city, type(city))
lst100 = [0] * 100
print(f'lst100 = [0]*100 {lst100}')
lst100 = [None] * 100
print(f'lst100 = [None]*100 {lst100}')

A = [[1, 2, 3, ], [4, 5, 6, ], [7, 8, 9]]
print(f'A[1][1] = {A[1][1]}')
print(f'A = {A}')

now_lst = [1, 2, 3, ] + ["Москва", "Питер", "Курск", "Орел"]
print(f'now_lst  = {now_lst}')
now_lst = ["number"] + now_lst
print(f'now_lst  = {now_lst}')

now_lst = now_lst + ["number"]
print(f'now_lst  = {now_lst}')

print(f'"number" in now_lst  = {"number" in now_lst}')

lst = [-1, 0, 5, 3, 2, 54, -34, 4, 8]

print(f'min(lst) = {min(lst)}, max(lst) = {max(lst)} ,sum(lst) = {sum(lst)} ')
print(f'sorted(lst) = {sorted(lst)}, reverse  sorted(lst) = {sorted(lst, reverse=True)} ')

b = [[1, 2, 3, ], [4, 5, 6, ], [7, 8, 9]]
print(f'b old {b}')
for x in range(len(b)):
    #print(f'x  = {x}, b[x] = {b[x]}')
    for y in range(len(b[x])):
        #print(f'x  = {x}, y  = {y}, b[x][y] = {b[x][y]}')
        b[x][y] = b[x][y] * 2
        print(f'x  = {x}, y  = {y}, b[x][y] = {b[x][y]}')

print(f'b new {b}')
