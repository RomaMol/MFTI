#!/usr/bin/python
# -*- coding: utf-8 -*-

#    https://youtu.be/F6ec1lipfUk?list=PLA0M1Bcd0w8zo9ND-7yEFjoHBg_fzaQ-B
#    20. ООП Python 3: распространение исключений (propagation exceptions)


def fun2():

    return 10/0
    # try:
    #     10 / 0
    # except ArithmeticError:
    #     print("-----Делить на ноль нельзя!----")


def fun1():
    return fun2()


print("Куда ты скачешь, гордый конь,")
print("И где опустишь ты копыта?")

try:
    print(fun1())
except ArithmeticError:
    print("-----Делить на ноль нельзя!----")

print("Не так ли ты над самой бездной")
print("На высоте, уздой железной")
print("Россию поднял на дыбы?")
