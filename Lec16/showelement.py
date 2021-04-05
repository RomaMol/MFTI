def showelement(lst, fun):
    for x in lst:
        if fun(x):
            print(x)



lst =(1,2,3,4,5,6,7,8,9)
def odd(x):
    return True if x%2!=0 else False

showelement(lst, odd)
