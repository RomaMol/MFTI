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
print(f'string_user.count("ra",4,11) = {string_user.count("ra",4,11)}')
print(f'string_user.count("ra", 4, 10) = {string_user.count("ra", 4, 10)}')

print(f'string_user.find("br",) = {string_user.find("br",)}')
print(f'string_user.find("brr",) = {string_user.find("brr",)}')
print(f'string_user.find("br",2) = {string_user.find("br",2)}')

print(f'string_user.replace("ab", "AB") = {string_user.replace("ab", "AB")}')
print(f'string_user.replace("ab", "") = {string_user.replace("ab", "")}')

# Третий необязательный аргумент задает максимальное количество замен. Например:

print(f'string_user.replace("ab", "AB") = {string_user.replace("ab", "AB")}')
print(f'string_user.replace("a", "o",2) = {string_user.replace("a", "0",2)}')

print(f'string_user.isalpha() = {string_user.isalpha()}')
print(f'string_user.isalpha() = {"string_user1212".isalpha()}')

print(f'string_user.isdigit() = {string_user.isdigit()}')
print(f'string_user.isdigit() = {"1212".isdigit()}')

print(f'string_user.rjust(4) ={"1212".rjust(4)}')
print(f'string_user.rjust(5) ={"1212".rjust(5)}')
print(f'string_user.rjust(7,"*") ={"1212".rjust(7,"*")}')

print(f'string_user.ljust(4) ={"1212".ljust(4)}')
print(f'string_user.ljust(5) ={"1212".ljust(5)}')
print(f'string_user.ljust(8,"*") ={"1212".ljust(8,"*")}')
fio = "Иванов Иван Иванович"
print(f'fio = {fio}')
print(f'fio.split(" ") ={fio.split(" ")}')

data = '1,34, 56 , 5677, rrr, 984'
new_data = data.replace(' ', '').split(',')
new_string = ', '.join(new_data)
print(f'data     {data}\nnew_data {new_data}')
print(f'new_data   {new_data}\nnew_string {new_string}')

string = '    rververver erverv rvre      \n'
print()
print(f'string {string}')
print(f'string.strip()  {string.strip()}')
print(f'string.rstrip() {string.rstrip()}')
print(f'string.lstrip() {string.lstrip()}')