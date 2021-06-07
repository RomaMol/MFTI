#!/usr/bin/python
# -*- coding: utf-8 -*-

#   https://www.youtube.com/watch?v=VxLzxh9B8EE
#   Python 3 #20: итераторы, выражения-генераторы, функции-генераторы, оператор yield

a = [x ** 2 for x in range(11)]  # Список из квадратов чисел от 0 до 10
print("Список из квадратов  [] ", a)

b = (x ** 2 for x in range(11))  # выражения-генераторы
print("выражения-генераторы () ", b)

it = iter(a)
print("Список -->iter(a) --> итераторы ", it)
for x in range(len(a)):
    print("next(it)", next(it))

# Для безконечно длинного списка
#       lst = list(range(1000000000))
#     MemoryError

lst = (x for x in range(1000000000))  # выражения-генераторы

for x in lst:
    print(x, end=" ")
    if x > 100: break
print("\n--------------------------")
for x in lst:
    print(x, end=" ")
    if x > 200: break
print("\n--------------------------")

b = (x ** 2 for x in range(11))  # выражения-генераторы
print("выражения-генераторы () max(b)  ", max(b))

b = (x ** 2 for x in range(11))
print("выражения-генераторы () min(b)  ", min(b))

b = (x ** 2 for x in range(11))
print("выражения-генераторы () sum(b)  ", sum(b))

print("выражения-генераторы () not len(b), not b[10]  ")

b = (x ** 2 for x in range(11))
a = list(b)
print("выражения-генераторы () ---> a = list(b)  ", a)
print("длина списка      len(a)  ", len(a))
print("элемент списка    a[7]    ", a[7] )
