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
bad_chars = 'а'

for chars in text:
    print('chars', chars)
    if chars == bad_chars :
        print("chars == bad_chars", chars)
    #print('chars', chars)

# for bad_chars in text:
#     print(bad_chars)
#     if bad_chars == 'a':
#         print("bad_chars == ", bad_chars)
#         for bad_chars in text:
#             if bad_chars == 'b':
#                 print("bad_chars == ", bad_chars)
#                 text2 = text2.append()


text2 = text.replace("ab", "")

print(f'удаление из строки "{text}"  "аb"  = {text2}')
