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
number = 0
text1 = ''
while number < len(text):
    print(number)
    if number + 1 >= len(text):
        chars1 = text[number]
        text1 = text1 + chars1
        print("chars1", chars1, "text1", text1)
        break
    else:
        chars1 = text[number]
        chars2 = text[number + 1]
        test = chars1 + chars2
        print("chars1", chars1, "chars2", chars2)
        print("test", test, "bad_chars", bad_chars)
        if test == bad_chars:
            chars1 = ''
            chars2 = ''
            number += 1
            # else:
        number += 1
        text1 = text1 + chars1
        print('text1', text1)

print(' while number < len(text):  text1', text1)

text2 = text.replace("ab", "")
print(f'удаление из строки "{text}"  "аb"  = {text2}')
