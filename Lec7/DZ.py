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
bad_chars1 = 'a'
bad_chars2 = 'b'

for number in range(0, len(text)):
    print(number)
    chars = text[number]
    # print('chars', chars)
    if chars == 'a':
        # print("chars == bad_chars a", chars)
        chars = ''
        # if number + 1 > len(text):
        #     break
        # else:
        #     if text[number + 1] == 'b':
        #         # print("chars == bad_chars b", chars)
        #         chars = ''

    print('chars', chars)

text2 = text.replace("ab", "")

print(f'удаление из строки "{text}"  "аb"  = {text2}')
