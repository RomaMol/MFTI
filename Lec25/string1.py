#!/usr/bin/python
# -*- coding: utf-8 -*-

#   https://youtu.be/ZzWdGLuq69E
#   Python 3 #25: форматирование строк: метод format и F-строки
#

name = "Fedot"
age = 18
mytext = "меня завут {fio}  и мне {vozrast} лет".format(fio=name, vozrast=age)
mytext2 = f"меня завут {name}  и мне {age} лет"
mytext3 = f"меня завут {name.upper()}  и мне {age+2} лет"

print(mytext)
print(mytext2)
print(mytext3)
