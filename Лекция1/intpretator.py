
def intpr():
    import this
    m = 2**1000
    print(m)
    print(type(m))
    print(dir(m))
    print(2+2 ==4)
    print(type(2 + 2 == 4))

    x= 2**10
    y = x
    print('x = 2*10  ', x,  'y =x ', y )
    s= y/13
    print(' s,type(s)  ',s,type(s))
    print('round(s), type(s)',round(s), type(s))
    s = int(y / 13)
    print('s = int(y / 13) s, type(s)', s, type(s))
    print(round(s), type(s))

    # print_hi('PyCharm')
    name = input('fest name  ')
    print(f'Hi, {name}')
    lastname = input('last name  ')
    print(f'Hi, {name}')
    print(f'Hi, {name + lastname}')