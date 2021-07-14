#!/usr/bin/python
# -*- coding: utf-8 -*-

#    https://www.youtube.com/watch?v=RUSk03GkE_Y&list=PLA0M1Bcd0w8zo9ND-7yEFjoHBg_fzaQ-B&index=19
#    19. ООП Python 3: введение в обработку исключений

def fun2():
    try:
        10/0
    except ArithmeticError:
        print("-----Делить на ноль нельзя!----")

def open_file():
    try:
        file = open("myfile2.txt")
    except FileNotFoundError:
        print(" --- Невозможно открыть файл  ---- ")

print("Куда ты скачешь, гордый конь,")
print("И где опустишь ты копыта?")
print(fun2())
print("Не так ли ты над самой бездной")
print("На высоте, уздой железной")
print("Россию поднял на дыбы?")



open_file()
