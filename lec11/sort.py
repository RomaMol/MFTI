#!/usr/bin/python
# -*- coding: utf-8 -*-

#   https://www.youtube.com/watch?v=gMM7632kTkI
#   Python 3 #11: списки - инструмент list comprehensions, сортировка методом выбора

# сортировка методом выбора
A=[2,9,43,6,34,68,4,2,4,54]
n = len(A)
for i in range(n-1):
    for j in range(i+1,n):
        if A[i]>A[j]:
            A[i], A[j] = A[j], A[i]

print(A)