#!/usr/bin/python
# -*- coding: utf-8 -*-

#   https://www.youtube.com/watch?v=nGEAfvtkCqc
#   Python 3 #7: строки - сравнения, срезы строк, базовые функции str, len, ord, in

# срезы

str3 = """ mnogo strok texta"""
print(f"len str3  {len(str3)}")

name1 = str3[5:12]
print(f"name1 = str3[5:10] ==  {name1}")

name2 = str3[5:]  # от 5 до конца
print(f"name2 = str3[5:] ==  {name2}")

name3 = str3[:5] # от нуля до
print(f"name3 = str3[:5] ==  {name3}")

name4 = str3[::2] # от нуля до конца с шагом 2
print(f"name3 = str3[:5] ==  {name4}")