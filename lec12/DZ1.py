# !/usr/bin/python
# -*- coding: utf-8 -*-


# print(dict([[i, int(i)**2] for i in input('Введите натуральное число: ').split() if int(i) % 2 == 0]))
d = dict()
N = 0  # количество чисел
x = 0  # вводимые числа

while x >= 0:
    x = input("Введите число: ")
    if x.isalpha():
        print("Введено не число")
        break
    else:
        x = int(x)
        print(f"x = {x} {x % 2}")
        if x % 2 == 0:
            d[x] = x ** 2
        print(d)

print(d)
