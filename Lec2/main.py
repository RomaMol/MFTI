#!/usr/bin/python
# -*- coding: utf-8 -*-

#   https://www.youtube.com/watch?v=NYJoyZHEW04
#   Python 3 #2: переменные, оператор присваивания, типы данных

#  = - связывания объекта """ "Helo World!!" """ или """ 5 """ с переменной  Х
x = "Helo World!!"
print(x)
print(id(x))
print(type(x))

x = 5
print(x)
print(id(x))
print(type(x))

#  =   оператор каскадного присваивания
a = b = c = 99
print('a = b = c = 99  оператор каскадного присваивания')
print('id(a) = ', id(a))
print('id(b) = ', id(b))
print('id(c) = ', id(c))
#  =   оператор множественного  присваивания
print()
a, b, c = 99, 34, 50
print('a,b,c = 99,34,50  оператор множественного  присваивания')
print('id(a) = ', id(a))
print('id(b) = ', id(b))
print('id(c) = ', id(c))

print('a,b ', a, b)
a, b = b, a
print('a,b = b,a оператор множественного перекрестного присваивания')
print('a,b ', a, b)
q= 10
print(f'q type(q), {q},  {type(q)}')
q= 10.3
print(f'q type(q), {q},  {type(q)}')
q = "Helo World!!"
print(f'q type(q), {q},  {type(q)}')

q = "Helo \'World!!\' wwww"
print(f'q type(q), {q},  {type(q)}')

q = True
print(f'q type(q), {q},  {type(q)}')