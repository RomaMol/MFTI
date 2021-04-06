def showelement(lst, fun):
    for x in lst:
        if fun(x):
            print(x)


lst = (1, 2, 3, 4, 5, 6, 7, 8, 9)


def odd(x):
    return True if x % 2 != 0 else False


showelement(lst, odd)

lambda_funk = lambda a, b: a + b
print(lambda_funk(10, 15))

showelement(lst, lambda x: True if x % 2 == 0 else False)
