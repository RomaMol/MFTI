#!/usr/bin/python
# -*- coding: utf-8 -*-

#   https://www.youtube.com/watch?v=bVYvtpMeepU
#   Python 3 #27: пакеты (package) - создание, импорт, установка (менеджер pip)
import mypakege

print(dir(mypakege))

print(mypakege.Name)
import mypakege.myonemodule

a = mypakege.myonemodule.onefun()