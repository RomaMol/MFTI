#!/usr/bin/python
# -*- coding: utf-8 -*-

#   https://www.youtube.com/watch?v=eWa_nwiE2PY
#   Python 3 #13: кортежи (tuple) и операции с ними: len, del, count, index

a = 1, 2, "tree", 4, "5"
lst = [1, 2, "tree", 4, "5"]
a1 = 12,
print(a, '\n', a1)
x, y = 1, 22
print(x, y)
print("len(a) = ", len(a))
print('tuples.__sizeof__()', a.__sizeof__(), 'lst.__sizeof__()', lst.__sizeof__())

b = tuple()
print('b =tuple() ', b)
b = b + ("tupl",)
print('b =  ', b)
b = a + b
print('b =  ', b)
c = (10,) * 10
print('c = (10,)*10 ==> ', c)
a1 = tuple("поисковый запрос")
print('tuple("поисковый запрос") ==> ',a1)
lst = list(a1)
print('lst = list(a1) ==> ',lst)
print('lst = list(a1) ==> ',["".join(lst)])

