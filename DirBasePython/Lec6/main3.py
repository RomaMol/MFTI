#!/usr/bin/python
# -*- coding: utf-8 -*-

#   https://www.youtube.com/watch?v=YY5cICJTDEU
#   Python 3 #6: операторы циклов while и for, операторы break и continue

# Вложенные циклы

A = [[1, 2, 3], [4, 5, 6]]
N = 2
M = 3
for i in range(N):
    for j in range(M):
        print(A[i][j], end="")
    print()

S = 0
M = 10
N = 5
for i in range(1, N + 1):
    print("i", i)
    for j in range(1, M + 1):
        print("j", j)
        S += i * j
        print("S += i*j ", S)
print(S)
