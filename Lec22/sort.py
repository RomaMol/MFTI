#!/usr/bin/python
# -*- coding: utf-8 -*-

#   https://youtu.be/uvlKcOS4OQw?list=RDCMUClJzWfGWuGJL2t-3dYKcHTA
#   https://www.youtube.com/watch?v=uvlKcOS4OQw&list=RDCMUClJzWfGWuGJL2t-3dYKcHTA
#   Python 3 #22: сортировка sort() и sorted(), сортировка по ключам

a = [1, 10, -45, 3, 55]
lst1 = ["Москва", "Сочи", "Курск", "Орел", "Новосибирск", "Архангельск", "Воронеж"]
a.sort()
print("a.sort() ", a)
lst1.sort()
print("lst1.sort()  ", lst1)
lst2 = ["Москва", "Сочи", "Курск", "Орел", "Новосибирск", "Архангельск", "Воронеж"]

print("sorted(lst2) ", sorted(lst2))
c = "Hellow world !!! brazers"
print("c=Hellow sorted(c) ", sorted(c))

lst2 = ["Москва", "Сочи", "Курск", "Орел", "Новосибирск", "Архангельск", "Воронеж"]

print("sorted(lst2) reverse=True", sorted(lst2, reverse=True))


# ----------------------------------------------------------

def funsort(x):
    if x % 2 == 0:
        return x
    else:
        return x + 100


a = (1, 2, 7, 10, -45, 3, 55, 4, 6)

print("sorted(a) key=funsort ", sorted(a, key=funsort))

a = (1, 2, 7, 10, -45, 3, 55, 4, 6)
print("sorted(a) key=funsort ", sorted(a, key=lambda x: x % 2))

lst2 = ["Москва", "Сочи", "Курск", "Орел", "Новосибирск", "Архангельск", "Воронеж"]
print("sorted(lst2) key=funsort      ", sorted(lst2, key=len, reverse=True))
print("sorted(lst2) lambda x:  x[0]  ", sorted(lst2, key=lambda x: x[0]))
print("sorted(lst2) lambda x:  x[-1] ", sorted(lst2, key=lambda x: x[-1]))
