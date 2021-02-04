def foo():
    pass


def foo1():
    return None


def foo2(x):  # формальные параметры
    return x ** 2


def foo3(a):  # формальные параметры
    a[0] = 7
    print('foo3(a) a[0]=7', a)
    a = [5, 6, 7]
    return a


def foo4(x, y, z=0):
    return 100 * x + 10 * y + 1 * z


def foo5(*args):
    for arg in args:
        print('arg in args  ', arg)


def foo6(*args, name_parameter='SEP'):
    for arg in args:
        print(name_parameter + ' arg in args  ', arg)


def foo7(*args, name_parameter='SEP'):
    a = args[0]
    print('arg in args  ', a)
    for arg in a:
        print(name_parameter + ' arg in args  ', arg)


def print_hi(name):
    # -------Функции----Локальные имена-----
    x = foo()
    print('x= foo()', x)
    x1 = foo1()
    print('x1= foo()', x1)
    x3 = foo2(5)  # фактические значения
    print('x1= foo()', x3)
    a = [1, 2, 3]
    print(' a = [1, 2, 3]', a)
    x4 = foo3(a)
    print('x4= foo(a)', a)
    print('foo4', foo4(1, 2, 3))
    print('foo4 z=1, y=2, x=3', foo4(z=1, y=2, x=3))
    print('foo4 z=1, y=2, x=3', foo4(x=1, y=2))

    print('foo5(*args):', foo5('www', 'eee', 'rrr'))

    foo6('www', 'eee', 'rrr', name_parameter='SEP')
    print()
    a = ['www', 'eee', 'rrr']
    foo7(a, name_parameter='SEP')


if __name__ == '__main__':
    print_hi('PyCharm')