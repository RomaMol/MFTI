#!/usr/bin/python
# -*- coding: utf-8 -*-

#   https://www.youtube.com/watch?v=Ccry8wMJ39o
#   Python 3 #23: обработка исключений: try, except, finally, else

x = input("x : ")
y = input("y : ")
try:
    x = int(x)
    y = int(y)
    rec = x / y
except ZeroDivisionError:
    rec = "Деление на ноль"
except ValueError:
    rec = "Введите число"
finally:
    print("Этот блок выполняется всегда")


print("rec = ", rec)
