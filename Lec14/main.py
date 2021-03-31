#!/usr/bin/python
# -*- coding: utf-8 -*-

#   https://www.youtube.com/watch?v=WElr9nSS6bo
#   Python 3 #14: функции (def) - объявление и вызов

def printHelow():
    print("Hellow world")


# printHelow()
p = printHelow
p()


def myxvkbd(x):
    x = x ** 2
    return x


print(myxvkbd(3))


def ispositive(p):
    if p >= 0:
        return True
    else:
        return False


lst = []
for p in range(-10, 10):
    if ispositive(p):
        lst.append(p)
print(lst)

lst1 = [1,2,-5,8,-12,4,-6,26]
lst2 = []
for p in lst1:
    if ispositive(p):
        lst2.append(p)
print(lst2)

def printHelow2(msg, end = " !!!"):
    #print("Hellow world")
    return print(msg + end)

printHelow2("Hellow world")
printHelow2("Hellow world", "  @@@@")