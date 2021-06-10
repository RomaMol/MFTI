#!/usr/bin/python
# -*- coding: utf-8 -*-

#   https://www.youtube.com/watch?v=bnxlN1veGzk
#   Python 3 #24: файлы - чтение и запись: open, read, write, seek, readline, dump, load, pickle
# 'file' = Путь к файлу вместе с именем
#  mode="r" режим чтения иди "w" запись файла
#  encoding=None  кодировка файла
# "test.txt"  --> D:\2020-PYTHON\MFTI\Lec24\test.txt

# D:\\2020-PYTHON\\MFTI\\Lec24\\test.txt -->  D:/2020-PYTHON/MFTI/Lec24/test.txt
# D:/2020-PYTHON/outtest.txt  --> ../outtest.txt
# D:/2020-PYTHON/2021Corpnet/intest.txt -->  ../2021Corpnet/intest.txt


# open('file',mode="r", encoding=None)
try:
    file1 = open('test.txt')
except FileNotFoundError:

    print("Файл ненайден")

