#!/usr/bin/python
# -*- coding: utf-8 -*-

#   https://www.youtube.com/watch?v=eWa_nwiE2PY
#   Python 3 #13: кортежи (tuple) и операции с ними: len, del, count, index

print("1 zadacha")
p = ("+792345678", "+792345478", "+692344678", "+592345678", "+392345678", "+7923456558")
print("spisok nomerov", p)
for i in p:
    if '+7' in i:
        print("v nomere '+7' =  ", i)

print("2 zadacha")
a = '5, 4, 3, 4, 2, 4, 5, 4'
print("dano stroka = ", a)
a1 = a.replace(', ', '')

tup_a = tuple(a1)
print("stroka = ", a, "\n", "ctroka bez ',' i probel' ' = ", a1, "\n", "tuple = ", tup_a)

print("3 zadacha")
a = ((1, 2, "me"), (False, 5, 6), (7, 8, 9))
print("dano kortage = ", a)
for el in a:
    for n in el:
        if el.index(n) < len(el) - 1:
            print(n, end='-')
        else:
            print(n)
