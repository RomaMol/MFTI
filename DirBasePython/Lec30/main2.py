#!/usr/bin/python
# -*- coding: utf-8 -*-

#   https://www.youtube.com/watch?v=xmRnm8bafwI
#   Python 3 #30: функция enumerate, примеры использования

for i in enumerate("hellow"):  # пример со строкой
    print(f"i = {i}")

for i in enumerate(["hellow", "world"]):  # пример со листом
    print(f"i = {i}")

slovar = {1: "hellow", 2: "world", 3: "geroi"}
for i in enumerate(slovar):  # пример со словарем виден ключ
    print(f"i = {i}")

mnogestvo = {1, "hellow", 2, "world", 3, "geroi"}
for i in enumerate(mnogestvo):  # пример со словарем виден ключ
    print(f"i = {i}")

slovar = {1: "hellow", 2: "world", 3: "geroi"}
print(f"slovar {slovar}")
for i, g in enumerate(slovar):  # пример со словарем виден ключ
    print(f"i = {i, g, slovar[g]}")
