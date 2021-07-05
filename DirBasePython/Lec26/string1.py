#!/usr/bin/python
# -*- coding: utf-8 -*-

#   https://youtu.be/M1EU-cR7-6s
#   Python 3 #26: создание и импорт модулей - import, from, as, dir, reload
#   https://docs.python.org/3/library/
#   https://pypi.org

import my_math
# import lib.my_math
from lib.my_math import summ_user

summ = my_math.summ_user(4, 6, 9)
print("summ ", summ)

# summ2 = lib.my_math.summ_user(4, 6, 9)
# print("summ2 ", summ2)

summ3 = summ_user(4, 6, 9)
print("summ3 ", summ3)
