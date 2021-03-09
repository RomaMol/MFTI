#!/usr/bin/python
# -*- coding: utf-8 -*-

#   https://www.youtube.com/watch?v=mlv2POHhZn8
#   Python 3 #5: условный оператор if, составные условия с and, or, not

# if <условное выражение истина>:
#     <выполняются какие то действия>
# else:
#     <выполняются какие то действия>
x = float(input("Введите число :"))
y = x
if x < 0:
    x = -x
print(x)

print("3>4", 3 > 4)
print('rbn > rkjbd', "rbn" > "rkjbd")
sgn = 0
if y < 0:
    sgn = y
    print("x- отрицательное число", sgn)
elif y > 0:
    sgn = y
    print("x- положительное  число", sgn)
else:
    sgn = 0
    print("x = 0", sgn)

# тернальнвй оператор
age = 15
penmen = True if age < 18 else False
penmen2 = age < 18
print(penmen, penmen2)

xy = 55
if 2 <= xy <= 7:
    print("2<=", xy, "<=7")
else:
    print(xy)

if xy <=2  or xy >= 7:
    print(xy)
else:
    print("2<=", xy, "<=7")