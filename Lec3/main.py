#!/usr/bin/python
# -*- coding: utf-8 -*-

#   https://www.youtube.com/watch?v=HrlUxTOxil4
#   Python 3 #3: функции input и print ввода/вывода

#
"""
работа  input()
input()
a = input()
print(a)
"""
"""
вычисляем периметр
w = int(input())
h = int(input())
p = (w+h)*2
print(p)
"""
"""
# вычисляем периметр
w = int(input("Введите ширину :"))
h = int(input("Введите длину  :"))
p = (w+h)*2
print(f'Периметр равен : {p}')
"""
# Форматный вывод функции  print
name = "fedia"
f_name = "dmitrii"
familia = "sokol"
age = 18
print("Фамилия: %s  Имя: %s  Отчество: %s  Возраст %d" % (familia, name, f_name, age), )
print(f'Фамилия: %s \nИмя: %s \nОтчество: %s \nВозраст %d' % (familia, name, f_name, age))
