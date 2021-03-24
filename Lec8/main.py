#!/usr/bin/python
# -*- coding: utf-8 -*-

#   https://www.youtube.com/watch?v=4LDjbKQS9PA
#   Python 3 #8: методы строк - upper, split, join, find, strip, isalpha, isdigit и другие


#  строка.имя_метода(аргументы)

string_user = "abrakadabra"
print(f'string_user.upper() = {string_user.upper()}')
print(f'string_user.lower() = {string_user.lower()}')

print(f'string_user.count("ra") = {string_user.count("ra")}')

# String.find(sub[, start[, end]])  count("ra", 4, 10)
print(f'string_user.count("ra", 4, 10) = {string_user.count("ra", 4, 10)}')

print(f'string_user.replace("ab", "AB") = {string_user.replace("ab", "AB")}')
print(f'string_user.replace("ab", "") = {string_user.replace("ab", "")}')

# Третий необязательный аргумент задает максимальное количество замен. Например:

print(f'string_user.replace("ab", "AB") = {string_user.replace("ab", "AB",1)}')
