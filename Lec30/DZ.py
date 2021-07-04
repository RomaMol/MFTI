#!/usr/bin/python
# -*- coding: utf-8 -*-

#   https://www.youtube.com/watch?v=xmRnm8bafwI
#   Python 3 #30: функция enumerate, примеры использования

A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"до применения функция enumerate {A}")
try:
    n = int(input(f"Введите число от 0 до 2 :"))
except:
    print("Неправильное число, Введите число от 0 до 2 : ")


def modelist():
    """изменение листа по заявленным правилам"""
    for element in enumerate(A):  # функция enumerate(spisok, start = 0) начальное значение индекса
        # print(f'картеж {element}')
        for i, g in enumerate(element):
            # print(f'element2 {g}')
            if isinstance(g, list):
                for i, x in enumerate(g):
                    # print(f'element2 {i, x}')
                    if i == n:  # порядковый элемент списка   [1, 2, 0]
                        g[i] = 0  # изменяем соответствующее значение  с 3 на 0 [1, 2, 0]
                        # print("g = ", g)
                    i += 1


modelist()
print(f" измененный список применения функция enumerate {A}")
