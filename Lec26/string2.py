#!/usr/bin/python
# -*- coding: utf-8 -*-

#   https://youtu.be/M1EU-cR7-6s
#   Python 3 #26: создание и импорт модулей - import, from, as, dir, reload
#   https://docs.python.org/3/library/
#   https://pypi.org

import math, time, random, os
import my_math
print(my_math.pi)
my_math.pi = 3
import my_math
print(my_math.pi)

# Перезагрузка модуля в программе после изменения значения в модуле
import importlib
importlib.reload(my_math)
print(my_math.pi)


print(dir(my_math))