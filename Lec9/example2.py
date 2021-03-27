#!/usr/bin/python
# -*- coding: utf-8 -*-

#   https://www.youtube.com/watch?v=ImWIDeW4GH0
#   Python 3 #9: списки list и функции len, min, max, sum, sorted

dig = [0] * 100
N = 0  # количество чисел
x = 0  # вводимые числа

while x >= 0:
    x = int(input("Введите число: "))
    dig[N] = x
    if x >= 0:
        N += 1

s = 0
for x in range(N):
    s += dig[x]

s = s / N
print(f'Среднее арифметическое: {s}, количестов {N}')
