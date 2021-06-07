#!/usr/bin/python
# -*- coding: utf-8 -*-

#   https://www.youtube.com/watch?v=VxLzxh9B8EE
#   Python 3 #20: итераторы, выражения-генераторы, функции-генераторы, оператор yield

def getallavage(N):
    """
    """
    avs = []
    count = 0
    summ = 0
    for x in range(1, N + 1):
        count += 1
        summ += x
        avs.append(summ / count)
    return avs


print("razmer in bait",getallavage(100).__sizeof__(),"  getallavage", getallavage(100),)

def ff1():
    """ yield x - замораживает цикл"""
    for x in range(10):
        yield x


print("ff1", ff1())
s = ff1()
for x in range(10):
    print("next(s) = ",next(s))


def getallavage2(N):
    """
    """
    count = 0
    summ = 0
    for x in range(1, N + 1):
        count += 1
        summ += x
        yield summ / count

print('getallavage2')
it = getallavage2(100)
for x in range(100):
    print(next(it), end="  ")

print('\n')