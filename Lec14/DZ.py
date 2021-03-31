#!/usr/bin/python
# -*- coding: utf-8 -*-

#   https://www.youtube.com/watch?v=WElr9nSS6bo
#   Python 3 #14: функции (def) - объявление и вызов

def PerSq(w, h, t):
    if t == "p":
        return 2 * (w + h), "perimetr"
    elif t == "s":
        return w * h, "Sqart"
    else:
        print("Введите формальный параметр p или s")


w = int(input("введите ширину: "))
h = int(input("введите длину: "))
t = input("введите p для расчета периметра или s для расчета площади ")

print(PerSq(w, h, t)[1], PerSq(w, h, t)[0])


def fun(*args):
    return max(args)


lst = (2, 3, 14, 16, 26, 4, 5, -5, 11)
print("list", lst)
print("lst max = ", fun(2, 3, 14, 16, 26, 4, 5, -5, 11))
