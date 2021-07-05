#!/usr/bin/python
# -*- coding: utf-8 -*-

#   https://www.youtube.com/watch?v=gMM7632kTkI
#   Python 3 #11: списки - инструмент list comprehensions, сортировка методом выбора


# получеине списка цифр из большого числа

y = x = int(input("Введите целое положительное число:"))

digs = []
print(x)
while x:
    digs.append(x % 10)  # берем последнее число
    x = x // 10  # отбрасываем  последнюю цифру число

digs.reverse()
print("digs.reverse()", digs)

digs1 = []
print(y)
while y:
    digs1 = [y % 10] + digs1  # берем последнее число и ставим вперед(еденицы - десятки -сотни- тысячи)
    y = y // 10  # отбрасываем  последнюю цифру число

print("digs1", digs1)
