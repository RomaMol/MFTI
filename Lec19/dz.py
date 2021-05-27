#!/usr/bin/python
# -*- coding: utf-8 -*-
def datainput():
    """Программа определяет число уникальных слов введенных с клавиатуры """
    a = input("Введите строку :")
    #a = ("   множества (set) и операции над ними: вычитание, пересечение, объединение, сравнение  "
    #     "вычитание, пересечение, объединение   ")
    a = a.strip()
    replase_element = (' ', '\n', '!', '?', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '=', '+', '_', ':', ';')
    for x in replase_element:
        a = a.replace(x, ',')
    a = a.replace(',,', ',')
    new_a = a.split(',')
    setA = list(set(new_a))

    print(a)
    print(len(new_a), new_a)
    print(len(setA), setA)


datainput()
