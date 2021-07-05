#!/usr/bin/python
# -*- coding: utf-8 -*-

#   https://www.youtube.com/watch?v=k9gIUAdEjYc
#   Python 3 #4: арифметические операторы: сложение, вычитание, умножение, деление, степень

#
a, b, c = 3, 7, 5
print("a+b+c", a + b + c)
print("a*b+c", a * b + c)
print("a/b+c", a / b + c)
print("a**b+c", a ** b + c)
print("a**b**c", a ** b ** c)
print("b/a", b / a)
print("b//a", b // a)
print("b%a", b % a)
b = b + 1

print("b = b+1", b)
b += 1
print("b+=1", b)
import math
mm = max(3,7, 23,8,22,11,14)
print('max(3,7, 23,8,22,11,14)', mm)
a =16
sq= math.sqrt(a)
print("a, sq= math.sqrt(a)",a,  sq, type(sq))