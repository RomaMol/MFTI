#!/usr/bin/python
# -*- coding: utf-8 -*-

#   https://www.youtube.com/watch?v=Qul_UT5nYrw
#   Python 3 #19: множества (set) и операции над ними: вычитание, пересечение, объединение, сравнение

# Множество set  - неупорядоченная коллекция уникальных элементов
a = {1, 4, 7, "hello", "344", 4, 7, "hello"}
print("множество a = ", a, "type(a)", type(a))
b = set()
print("множество b = ", b, "type(b)", type(b))
c = set('hellow world')  # итерируемый объект - преобразуемый в множество поэлементно
print("множество c = ", c)
a = {1, 4, 7, "hello", "344", 4, 7, "hello"}
a = list(set(a))
print("множество a = ", a)

# Обратиться к элементам множества
setA = {1, 4, 7, "hello", "344", 4, 7, "hello"}
for x in setA:
    print("setA  x =", x)
# Добавление елементов в множество
setA.add(12)
setA.update([23, 45, "eee"])  # [] - как список
print("setA  ", setA)

# Удаление елементов в множество
setA.discard(23)
setA.discard(23)
print("setA  ", setA)
setA.remove(45)
# setA.remove(45)  KeyError: 45
print("setA  ", setA)
setA.clear()
print("setA  ", setA)
# Операции над множествами
setA = {1, 4, 7, "hello", "344", 4, 7, "hello"}

print("len setA", len(setA))
print("поиск в множестве", "hello" in setA)
print("поиск в множестве", "helfffo" not in setA)

setA = {1, 4, 7, "hello", "344", 4, 7, "hello",2,22}
setB = {1, 4, 7, "hello", "344", 34, 56, "bay"}

print("общее для двух множеств через & setA & setB ", setA & setB)
print("общее для двух множеств через setA.intersection(setB)", setA.intersection(setB))
print()
print("объединение  для двух множеств через setA | setB)", setA | setB)
print()
print("вычитание  для двух множеств через setA - setB", setA - setB)
print("вычитание  для двух множеств через setB - setA", setB - setA)
print()
print("удалеине одинаковых элементов из общего  setA ^ setB", setA ^ setB)
print()
print("сравнеине множеств   setA == setB", setA == setB)
print("сравнеине множеств   setA != setB", setA != setB)
print()
print("Вхождение  множеств   setA > setB", setA > setB)