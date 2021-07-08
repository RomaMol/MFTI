def cikl():
    x = int(input('Введи число  '))
    y = int(input('Введи число  '))
    # y = x+7 > x+2*x**3**x
    # y = x + 7 > x + (2 * (x ** (3 ** x)))
    # print(f'Hi, {type(y)}')
    while True:
        x = x - 1  # декремент
        # x = x+1 # инкркмент
        if x < 0:
            break
        print('x = ', x)
    print('end')

    while y >= 0:
        print('y = ', y)
        y -= 1  # декремент
        print('new y = ', y)
    print('end')


    # a = range(start:stop:step)
    a = range(0, 100, 10)

    for z in a:
        print(z)  #z = step

    for z in range(0,10,1): #range(start:stop:step)
        print(z) # z = step

    x = int(input('Введи число X '))
    y = int(input('Введи число Y '))
    if y > 0:
        if x > 0:
            print("A")
        else:
            print("B")
    else:
        if x > 0:
            print("D")
        else:
            print("C")

    x = int(input('Введи число X '))
    y = int(input('Введи число Y '))

    if x > 0 and y > 0:
        print("A")
    elif x < 0 and y > 0:
        print("B")
    elif x > 0 and y < 0:
        print("D")
    elif x < 0 and y < 0:
        print("C")
    else:
        print("Ось координат")