
def tup_user():
    x = 2  # связывания
    print("x  ", x)
    y = x  # y --> 2
    print("y  ", y)
    x += 1
    print("x = х+1 ", x)
    print("y  ", y)  # не изменяется

    x = y = z = 0  # 1 вариант
    x, y, z = 1, 2, 'name'  # 2 вариант
    print("x, y, z =  ", x, y, z)
    x, y = y, x  # обмен переменными
    print("обмен переменными x, y, z =  ", x, y, z)
    # --------------------Кортежи-----------------

    kortege = 1, 2, 3, 4, 5
    print(type(kortege))  # <class 'tuple'>
    print(kortege)  # (1, 2, 3, 4, 5)
    a, b, c, d, e, = kortege
    print("a,b,c,d,e, = kortege  ", a, b, c, d, e)  # 1 2 3 4 5
    a, b, *rest, = kortege
    print(" a, b, *rest,  ", a, b, *rest)  # 1 2 3 4 5
    print(" *kortege ", *kortege, '   sep=":"', sep=":", end=' !\n')

    ran = range(10)  # start, stop, step
    print(type(ran))
    print(*ran)
    for x in ran:
        print(x)

    l_user = [1, 2, 3]  # ЛИСТ
    l_user1 = [(10, 20), (20, 20), (30, 20)]  # ЛИСТ  с кортежами

    print('l_user1', l_user1)
    l_user1.append((40, 30))
    print('l_user1.append((40, 30))', l_user1)

    for i in range(len(l_user)):
        lenna, anglle = l_user1[i]
        print('lenna, anglle =  l_user[i]', l_user1[i])

    for tup in l_user1:  # tup = (10, 20)
        print('tup', tup)

    for lenna, anglle in l_user1:
        print('lenna, anglle  ', lenna, anglle)

    for i, x in enumerate(l_user):
        print('i, x  ', i, x)

    # --------------------Кортежи-----------------