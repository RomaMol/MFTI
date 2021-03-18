#!/usr/bin/python
# -*- coding: utf-8 -*-

#   https://www.youtube.com/watch?v=nGEAfvtkCqc
#   Python 3 #7: строки - сравнения, срезы строк, базовые функции str, len, ord, in

# строки
str1 = "stroka1 "
str2 = 'stroka2'
str3 = """ mnogo
strok texta"""
str4 = ''' mnogo strok
texta'''

print(f'str1   {str1},str2  {str2},')
print(f'str3   {str3}')
print(f'str4   {str4},')

# соеденяем только строки
msg = str1 + " " + str2
print(f'msg = str1 +" "+str2  ===  {msg},')

# дублирование строки
print(f'дублирование строки str1*10 {str1 * 10}')
n = str1 * 10

print(f"длина строки n = str1*10 len(n) =={len(n)}")

print(f"проверка содержания strok in n  ==  {'strok' in n}")
print(f"проверка содержания eeddt in n  ==  {'eeddt' in n}")

# проверка пароля

pws = "pass"
inp_pws = ""

while pws != inp_pws:
    inp_pws = input("Введите пароль:  ")
print("Hellow User")
