#!/usr/bin/python
# -*- coding: utf-8 -*-

#   https://www.youtube.com/watch?v=xmRnm8bafwI
#   Python 3 #30: функция enumerate, примеры использования
spisok1 = [1, 2, 7, 8, 66, 9]
spisok2 = [1, 2, 7, 8, 66, 9]
spisok3 = [1, 2, 7, 8, 66, 9]

for x in spisok1:
    print(x)
    x = 1

print(spisok1)

print(f'список до изменения    {spisok2}')
for i, x in enumerate(spisok2):  # функция enumerate(spisok, start = 0)
    if x % 2 == 0:
        spisok2[i] += 1

print(f'список после изменения {spisok2}')

print(f'список до изменения    {spisok3}')
for element in enumerate(spisok3, 3):  # функция enumerate(spisok, start = 0) начальное значение индекса
    print(f'картеж  -  позиция в списке и значение   {element}')

print(f'список до изменения    {spisok3}')
g = enumerate(spisok3)
print(f'g = enumerate(spisok3)   {g}')  # итерируемый объект

print(f'next(g)   {next(g)}')
print(f'next(g)   {next(g)}')


def enumerate2(spisok, start=0):
    n = start
    for elem in spisok:
        yield n, elem
        n += 1


for element in enumerate2(spisok1):  # функция enumerate(spisok, start = 0) начальное значение индекса
    print(f'картеж  -  позиция в списке и значение   {element}')
