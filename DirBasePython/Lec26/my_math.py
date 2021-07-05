pi = 3.14


def max_user(a, b):
    return a if (a > b) else b


def max3_user(a, b, c):
    return max_user(a, max_user(b, c))


def summ_user(*vals):
    print("lec26 ")
    print("summa = ")
    s = 0
    for x in vals:
        s += x
    return s
