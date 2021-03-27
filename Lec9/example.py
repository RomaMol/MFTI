#!/usr/bin/python
# -*- coding: utf-8 -*-

#   https://www.youtube.com/watch?v=ImWIDeW4GH0
#   Python 3 #9: списки list и функции len, min, max, sum, sorted


lst = [-1, 0, 5, 3, 2]
print(f'lst {lst}')
for x in range(5):
    print(f'x = {x}, lst[x] = {lst[x]},   lst[x]*7.2 = {lst[x] * 7.2} ')
print(lst)
print()


s1 = [-1, 0, 5, 3, 2]
print("ewcwecfwecfe", [i + 7.2 for i in s1])

for x in range(len(lst)):
    lst[x] = lst[x] * 7.2
    print(f'x = {x}, lst[x]*7.2 = {lst[x]}')
print(lst)
print()
nlst = []
for x in lst:
    x = int(x / 7.2)
    print(f'x = {x}')
    nlst.append(x)
print(f'lst {lst}')
print(f'nlst {nlst}')

m1 = [[1, 2], [3, 4], [5, 6]]
m2 = [[1, 0], [0, 1], [1, 1]]
m3 = m1
print(f'm1 + m2  = {m1},+ {m2}')

for i in range(len(m3)):
    print(f'i =  {i}')
    m3[i][0] = m1[i][0] + m2[i][0]
    m3[i][1] = m1[i][1] + m2[i][1]

print("summ matr",m3)

x = [1, 2, 3, 4, 5, 6]
y = [1, 0, 0, 1, 1, 1]
print('summ matr',[(x[i] + y[i]) for i in range(len(x))])
