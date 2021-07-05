#!/usr/bin/python
# -*- coding: utf-8 -*-

#   https://www.youtube.com/watch?v=YY5cICJTDEU
#   Python 3 #6: операторы циклов while и for, операторы break и continue

# for <переменная> in <список> :
#      операторы 1…N
for x in 1, 3, 6, 9:
    y = x * 2
    print(x, y)

# Для этого используется генератор последовательностей

# range(start, stop, step) начальное значение, шаг, конечное значение
# прямая последовательность
for x in range(0, 50, 5):
    print("прямая последовательность ", x)

# обратная  последовательность
for x in range(50, 0, -10):
    print("обратная  последовательность ", x)

S = 0
for i in range(1, 1001, 1):
    S += 1 / i
print(S)

S1 = 0
for i in range(1, 1001, 1): S1 += 1 / i
print(S1)

k = 0.5
b = 2
lst = [0, 0.1, 0.2, 0.3, 0.4, 0.5]
for x in lst:
    print(x * k + b)

msg = "Hello World!"
for x in msg:
    print(x)