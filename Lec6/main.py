#!/usr/bin/python
# -*- coding: utf-8 -*-

#   https://www.youtube.com/watch?v=YY5cICJTDEU
#   Python 3 #6: операторы циклов while и for, операторы break и continue

# S = 0  # нечто что выполняется
# i = 0  # счетчик цикла
# while i < 100:
#     """выполнять цикл по счетчик удовлетворяет условию i < 100"""
#     S = i / (1 + i)
#     print(S)
#     i += 1
# print(S)
s = 0  # нечто что выполняется
i = -11  # счетчик цикла
while i < 100:
    """выполнять цикл по счетчик удовлетворяет условию i < 100"""
    if i == 0:
        break
    s += 1 / i
    i += 1
else:
    print("Сумма ", s, "вычислена корректно")

print(s, " i == 0  сработал break")
#  цикл для целых чисел от -4 до 4 без 0
s = 0
i = -5
while i < 4:
    i += 1
    if i == 0:
        continue
    s += 1 / i

    print(i, "   ", s)
print(" the end", s)
