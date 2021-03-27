#!/usr/bin/python
# -*- coding: utf-8 -*-

#   https://www.youtube.com/watch?v=4LDjbKQS9PA
#   Python 3 #8: методы строк - upper, split, join, find, strip, isalpha, isdigit и другие

# dig = input("введите число: ")
# if dig.isdigit():
#     dig = int(dig)
#     print("число: ", dig)
# else:
#     print("Введено не число")


data = '1,34, 56 , 5677, rrr, 984'
new_data = data.replace(' ', '').split(',')
new_string = ', '.join(new_data)
print(f'data     {data}\nnew_data {new_data}')
print(f'new_data   {new_data}\nnew_string {new_string}')
