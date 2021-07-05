#!/usr/bin/python
# -*- coding: utf-8 -*-

#   https://www.youtube.com/watch?v=v8Q6nR7itsU
#   Python 3 #10: списки - срезы и методы: append, insert, pop, sort, index, count, reverse, clear


# lst = []
# while True:
#     x = int(input("Введите число: "))
#     if x != 0:
#         lst.append(x ** 2)
#     else:
#         break
# print(f'Список квадратов введенных чисел{lst}')

tel = ["+79121231456", "+79151231456", "+69121231456", "+49121231456", "+79121231456"]
tel1 = []
for x in tel:
    if x.find("+7") == 0:  # есть  +7
        tel1.append(x)
print(" есть  +7 tel1 = ", tel1)

tel = ["+79121231456", "+79151231456", "+69121231456", "+49121231456", "+79121231456"]
tel1 = []
for x in tel:
    if x.find("+7") == -1:  # нет  +7
        tel1.append(x)
print(" нет  +7 tel1 = ", tel1)

tel = ["+79121231456", "+79151231456", "+69121231456", "+49121231456", "+79121231456"]
print("3 variant", [i for i in tel if "+7" not in i])

spisok = [1, 2, 3, 4, 5, 6]
sdvig = int(input('Input the number of move: '))
print(f'spisok {spisok}')
for i in range(sdvig):
    print("for i in", i, "range(sdvig)", range(sdvig))
    n = spisok.pop(0)
    print(n)
    spisok.append(n)
print(spisok)
