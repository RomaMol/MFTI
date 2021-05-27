#!/usr/bin/python
# -*- coding: utf-8 -*-

#   https://www.youtube.com/watch?v=RRro03hYoQU
#   Python 3 #18: области видимости переменных - global, nonlocal

# Глобальные переменные в начале программы
a = 5
N = (100, 200)
HEIGHT, WIDTH = 100, 200


# Локальные переменные в функциях

def locfyn(b):
    """локальные переменные это b,x,n"""
    global a  # указывает на то как работать с переменной -- как с глобальной
    a = 10
    for x in range(b):
        n = x + 1
        print("n =", n, end="   ")


locfyn(6)
print('\n\n%d' % a, "\n", "a =", a)
Name = "TOM"


def sethellow():
    print("Hello ", Name)


def setBay():
    Name = "BOB"
    print("Hello ", Name)


sethellow()
setBay()

# nonlocal
x = 0


def outer():
    x = 1

    def inner():
        nonlocal x
        x = 2
        print("inner() x = ", x)

    inner()
    print("outer() x = ", x)



print("global  x = ", x)
outer()
