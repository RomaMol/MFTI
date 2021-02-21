from cortege import tup_user


def print_name(name: str, n=int):
    for i in range(n):
        print('hello', name)


def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    # print_name("name", 4)
    # tup_user()
    # ----------множества- set  словари- dict-----------------

    s = {'www', 'ver', 12, 'mos'}  # множества- set

    s.add('rost')

    if 'wwwq' in s:
        print('yes  wwwq')
    else:
        print('not  wwwq')

    for elen in s:
        print('elen', elen)
    # ----  словари- dict ----------------
    d = {'www': 222, 'ver': 121, '12': 333, 'mos': 454}
    print('d', d)
    d['wwwq'] = 234
    print('d[wwwq] = 234', d)

    for key in d:
        print('key  ',key)
        print('d[key]  ',d[key])


if __name__ == '__main__':
    print_hi('PyCharm')
