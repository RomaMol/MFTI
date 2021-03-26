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
    # print(number)
    if number + 1 >= len(text):
        chars1 = text[number]
        text1 = text1 + chars1
        #print("chars1", chars1, "text1", text1)
        break
    else:
        chars1 = text[number]
        chars2 = text[number + 1]
        test = chars1 + chars2
        # print("chars1", chars1, "chars2", chars2)
        # print("test", test, "bad_chars", bad_chars)
        if test == bad_chars:
            chars1 = ''
            chars2 = ''
            number += 1

        number += 1
        text1 = text1 + chars1
        # print('text1', text1)
print(f'решение через циклы text = {text}  text1 =  {text1}')

text2 = text.replace("ab", "")
print(f'решение через .replace("ab", "") "{text}"  "аb"  = {text2}')

bad_chars1 = 'ra'
number = 0
text4 = ''
while number < len(text):
    # print(number)
    if number + 1 >= len(text):
        chars1 = text[number]
        text4 = text4 + chars1
        #print("chars1", chars1, "text1", text1)
        break
    else:
        chars1 = text[number]
        chars2 = text[number + 1]
        test = chars1 + chars2
        # print("chars1", chars1, "chars2", chars2)
        # print("test", test, "bad_chars", bad_chars1)
        if test == bad_chars1:
            chars1 = ''
            chars2 = ''
            number += 1

        number += 1
        text4 = text4 + chars1
        # print('text1', text1)
print(f'решение через циклы text = {text}  text4 =  {text4}')

text3 = text.replace("ra", "")
print(f'решение через .replace("ra", "") "{text}"  "ra"  = {text3}')