#!/usr/bin/python
# -*- coding: utf-8 -*-

#   https://www.youtube.com/watch?v=gMM7632kTkI
#   Python 3 #11: списки - инструмент list comprehensions, сортировка методом выбора


# list comprehensions

a = []
n = 10
for x in range(n):
    a.append(x ** 2)

print(f'A = {a}')

m = 10
a = [x ** 2 for x in range(m)]

print(f'A = {a}')

a = [x ** 2 for x in range(m) if x % 2 == 0]
# 'элемент списка  + цикл вкотором будет формироваться элементы + условие для занесения элемента в список
print(f'A = {a}')
lst = ['Москва', "Питер", "Сочи", "Курск", "Орел", "Сочи", "Владимир", "Астрахань"]

a = [x for x in lst if len(x) <= 5]
print(f'lst = {lst}')
print(f'len(x)<=5 A = {a}')
