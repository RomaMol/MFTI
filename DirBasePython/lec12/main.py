#!/usr/bin/python
# -*- coding: utf-8 -*-

#   https://www.youtube.com/watch?v=XNzKPF5BPCw
#   Python 3 #12: словарь, методы словарей: len, clear, get, setdefault, pop


lst = [[1, 'Москва'], [2, "Питер"], [3, "Сочи"], [4, "Курск"], [5, "Орел"], [6, "Сочи"], [7, "Владимир"],
       [8, "Астрахань"]]

d = dict(lst)
print(f'lst =  {lst}')
print(f'dict(lst) =  {d}')
d2 = {1: 'Москва', 2: 'Питер', 3: 'Сочи', 4: 'Курск', 5: 'Орел', 6: 'Сочи', 7: 'Владимир', 8: 'Астрахань'}
d3 = dict.fromkeys([1, 2,'Питер', 4, 5, 6, 7, 8, '9'], 'City')
print(f'dict.fromkeys() =  {d3}')
d4 = {True:1, False:"Ложь", "point":[10,30,20], 5:50}
print(f'dict4 =  {d4}')
del d4[False]
print(f'del d4[False]=  {d4}')
d4[False] = "Ложь"
print(f'd4[False] = "Ложь"  =  {d4}')

print(f'"abc" in d4 =  {"abc" in d4}')

print(f'len(d4) =  {len(d4)}')

for x in d4:
    print(f'ключи словаря x = {x}') # ключи словаря

for x in d4:
    print(f'значения словаря d4[x]  = {d4[x]}') # значения словаря

d5 = d4.copy()
d4.clear()
print(f' d5 = d4.copy() = {d5 }, d4.clear() = {d4}')
d5.get('point')
print(f' d5.get("point") = {d5.get("point") } , d5.get("poi") = {d5.get("poi", "Нет такого ключа в словаре")}')

# Удаление несуществующего ключа из словаря

print(f'd5.pop("poi","Нет такого ключа в словаре" ) = {d5.pop("poi", "Нет такого ключа в словаре")}')
print(f' d5.keys() = {d5.keys() }, d5.values() = {d5.values()}, d5.items() = {d5.items()}')

for x in d5.items():
    print(f'd5.items()  x[0], x[1] = {x[0]}, {x[1]}') # ключи словаря + значения словаря

for key, value in d5.items():
    print(f'd5.items()  key, value = {key}, {value}') # ключи словаря + значения словаря