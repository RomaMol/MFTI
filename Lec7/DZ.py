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
new_text = []
for number in range(0, len(text)+1):
    chars = text[number]
    # print('chars', chars)
    if chars == 'a':
        print("chars == bad_chars a", chars)
        new_text = new_text.append()
        if text[number + 1] == 'b':
            print("chars == bad_chars b", chars)
            new_text = new_text.append()
    new_text = new_text.append()
    print('chars', chars, new_text)

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
