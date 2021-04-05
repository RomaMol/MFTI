#!/usr/bin/python
# -*- coding: utf-8 -*-

#   https://www.youtube.com/watch?v=z6b_F3OC39s
#   Python 3 #16: рекурсивные и лямбда-функции, функции с произвольным числом аргументов


def mysumm(*args):
    s = 0
    for x in args:
        s+=x
    return ("summa = ", s)

print(mysumm(1,3,5,3,8,0))

def muslov(**args):
    for name, vavue in args.items():
        print(name, vavue)

muslov(arg1=1,fname="igor", name="serga")

def muslov(*lst, **args):
    
    for x in lst:
        print(x , end=" ")
    print()
    for name, vavue in args.items():
        print(name, vavue)

muslov(10,20,45, arg1=1,fname="igor", name="serga")