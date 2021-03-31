#!/usr/bin/python
# -*- coding: utf-8 -*-

#   https://www.youtube.com/watch?v=_BDvZcqNgMw
#   Python 3 #15: делаем "Сапер", проектирование программ "сверху-вниз"
import random

N, M = (5, 15)  # N игровое поле N*N ,M количество мин


def gettotalmins(PM, i, j):
    """для расчета мин расположенных вокруг клетки"""
    boom = 0
    for k in range(-1, 2):
        for l in range(-1, 2):
            x = i + k
            y = j + l
            if x < 0 or x >= N or y < 0 or y >= N:
                continue
            if PM[x * N + y] < 0:
                boom += 1
    return boom


def creategame(PM):
    """создание поля с элементами"""
    rnd = random.Random()

    n = M
    while n > 0:
        i = rnd.randrange(N)  # случайное целое от 0 до  N по горизонтали
        j = rnd.randrange(N)  # случайное целое от 0 до  N по вертикали
        if PM[i * N + j] != 0:
            continue
        else:
            PM[i * N + j] = -1
        n -= 1
    # количество мин вокруг клетки
    for i in range(N):
        for j in range(N):
            if PM[i * N + j] == 0:
                PM[i * N + j] = gettotalmins(PM, i, j)


def show(pole):
    """отображения поля"""
    for i in range(N):
        for j in range(N):
            print(str(pole[i * N + j]).rjust(3), end='')

        print()


def goplaer():
    """запрос у игрока координат поля """
    flloopplaer = True
    while flloopplaer:
        x, y = input("введите координаты через пробел:").split()
        if not x.isdigit() or not y.isdigit():
            print("координаты введены неверно")
            continue

        x = int(x) - 1
        y = int(y) - 1
        if x < 0 or x >= N or y < 0 or y >= N:
            print("координаты за пределами поля")
            continue
        flloopplaer = False
    print(x, y)
    return (x, y)


def isfinish(PM, P):
    """проверка состояния продолжить игру или закончить"""
    for i in range(N * N):
        if P[i] != -2 and PM[i] < 0:
            return -1
    for i in range(N * N):
        if P[i] == -2 and PM[i] >= 0:
            return 1
    return -2


def startgames():
    """запуск программы, отрисовывание поля проверка работы"""
    P = [-2] * N * N  # В начале игры все клетки закрыты
    PM = [0] * N * N  # расстановка мин на поле закрытые мины
    creategame(PM)
    finstate = isfinish(PM, P)
    while finstate > 0:
        show(P)
        x, y = goplaer()
        P[x * N + y] = PM[x * N + y]
        finstate = isfinish(PM, P)


res = startgames()
if res == -1:
    print("вы проиграли")
else:
    print("вы выиграли")

print("game over")
