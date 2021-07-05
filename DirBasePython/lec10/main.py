#!/usr/bin/python
# -*- coding: utf-8 -*-

#   https://www.youtube.com/watch?v=v8Q6nR7itsU
#   Python 3 #10: списки - срезы и методы: append, insert, pop, sort, index, count, reverse, clear

lst = ['Москва', "Питер", "Курск", "Орел"]

# срезы и методы список[start:end]

print(f'lst[1:3] = {lst[1:3]}') # срез с 1 до 3 элемента не включая 3 элемент
print(f'lst[1:] = {lst[1:]}') # срез с 1  элемента
print(f'lst[:4] = {lst[:3]}') # срез до 3 элемента
print(f'lst[:] = {lst[:]}')  # срез полного списка
c= list(lst)
print(f'c= list(lst) =  {c}')
print(f'id(c) =  {id(c)} id(lst) =  {id(lst)}') # копия списка иднт разные

print(f'lst[::2] = {lst[::2]}') # шаг следование через 1 каждый второй
print(f'lst[::2] = {lst[::-1]}') # шаг следование через 1 каждый второй

# присвоение срезу новых значений
print(f'lst = {lst}')
lst[1:3] = 'Владимир', "Астрахань"

print(f'lst[1:3] = "Владимир", "Астрахань" = {lst}')
del lst[1]
print(f' del lst[1]" = {lst}')

# добавление элементов в конец списка

lst1 = ['Москва', "Питер", "Курск", "Орел", "Сочи"]
print(f' lst1.append("Сочи") = {lst1}')

# добавление элементов в  списка
lst1.insert(1,"Сочи")
print(f' lst1.insert(1,"Сочи") = {lst1}')

# добавление элементов в начало списка
lst1.insert(0,"Сочи")
print(f' lst1.append("Сочи") = {lst1}')

# удаление элемента по значению
lst1.remove("Сочи")
print(f' lst1.remove("Сочи") = {lst1}')

# удаление элемента по значению

print(f' lst1.pop()) = {lst1.pop()}\n'
      f'lst1 = {lst1}')
# удаление элемента по значению

print(f' lst1.clear() = {lst1.clear()}\n'
      f'lst1 = {lst1}')

lst1 = ['Москва', "Питер", "Сочи", "Курск", "Орел", "Сочи"]
# поиск элементов с одинаковым значением

print(f' lst1.count("Сочи") = {lst1.count("Сочи")}')

print(f' lst1.index("Сочи") = {lst1.index("Сочи")}')

print(f' lst1.reverse() = {lst1}')
print(f' lst1.reverse() = {lst1.reverse()}')
print(f' lst1.reverse() = {lst1}')

print(f' lst1.sort() = {lst1.sort()}')
print(f' lst1 = {lst1}')
print(f' lst1.sort(reverse=True) = {lst1.sort(reverse=True)}')

print(f' lst1 = {lst1}')