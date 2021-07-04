#!/usr/bin/python
# -*- coding: utf-8 -*-

#   https://www.youtube.com/watch?v=xmRnm8bafwI
#   Python 3 #30: функция enumerate, примеры использования

A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for element in enumerate(A):  # функция enumerate(spisok, start = 0) начальное значение индекса
    # print(f'картеж {element}')
    for i, g in enumerate(element):
        # print(f'element2 {g}')
        if isinstance(g, list):
            for i, g in enumerate(g):
                print(f'element2 {i, g}')
                if i == 0:
                    g = 0
                    print(g)
                i += 1

print(A)