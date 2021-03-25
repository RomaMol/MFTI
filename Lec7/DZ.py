#!/usr/bin/python
# -*- coding: utf-8 -*-
import re

text = "abrakadabra"

# подсчет буквы "а"
buk_va = "a"
kol_vo = 0
for x in text:
    if x == buk_va:
        kol_vo += 1
print(f'подсчет буквы "а" количество = {kol_vo}')

#  удаление из строки "аb"
bad_chars = 'ab'

new_text = ''
number = 0
print("len(text)", len(text))
while number < len(text):
    print(number)
    chars1 = text[number]
    if number + 1 >= len(text):
        break
    else:
        chars2 = text[number + 1]
        print("chars1 == bad_chars1[0]", chars1)
        print("chars2 == bad_chars1[1]", chars2)
        test = chars1 + chars2
        print("test = ", test, 'bad_chars = ', bad_chars)
        if test == bad_chars:
            number += 1
            chars1 = ''
            chars2 = ''
    if number <= len(text):
        number += 1
        new_text = new_text + chars1
    else:
        new_text = new_text + chars2

    print('chars', chars1, chars2, new_text)

text2 = text.replace("ab", "")

print(f'удаление из строки "{text}"  "аb"  = {text2}')
