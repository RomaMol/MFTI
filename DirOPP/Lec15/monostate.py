#!/usr/bin/python
# -*- coding: utf-8 -*-

#    https://www.youtube.com/watch?v=voRJv-t2SiA&list=PLA0M1Bcd0w8zo9ND-7yEFjoHBg_fzaQ-B&index=15

#    15. ООП Python 3: Моносостояние экземпляров класса


# пример реализации Моносостояния

class Trenddata:
    """класс для некого числа одинаковых потоков"""
    __common_attrs = {"name": "trend_1",
                      "data": {},
                      "id": 1
                      }

    def __init__(self):
        self.__dict__ = Trenddata.__common_attrs


td1 = Trenddata()
td2 = Trenddata()
print(f"td1.id = {td1.id}, td2.id = {td2.id}")
td1.id = 3
print(f"td1.id = 3 ")

print(f"td1.id = {td1.id}, td2.id = {td2.id}")

td2.new_attr = "new attr"
print(f"    td2.new_attr =  ")
print(f"td1.__dict__ = {td1.__dict__}")
print(f"td2.__dict__ = {td2.__dict__}")

print(f"id td1 = {id(td1.__dict__)}, id td2 = {id(td2.__dict__)}")