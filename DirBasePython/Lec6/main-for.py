#!/usr/bin/python
# -*- coding: utf-8 -*-

#   https://www.youtube.com/watch?v=YY5cICJTDEU
#   Python 3 #6: операторы циклов while и for, операторы break и continue

# for <переменная> in <список>:
#    <оператор>

for x in 1, 5, 2, 4:
    print(x ** 2)

# Для этого используется генератор последовательностей
# range(start, stop, step)
# прямая последовательность
for x in range(1, 5, 1):
    print("прямая последовательность  ", x)

# обратная последовательность
for x in range(5, 0, -1):
    print("обратная последовательность  ", x)

S = 0
for i in range(1, 1001, 1):
    S += 1 / i
print(S)

k = 0.5
b = 2
lst = [0, 0.1, 0.2, 0.3, 0.4, 0.5]
for x in lst:
    print(f"k {k}, b {b}, x {x}, lst{lst}")
    print("x*k+b", x * k + b)

msg = "Hello World!"
for x in msg:
    print(x)
