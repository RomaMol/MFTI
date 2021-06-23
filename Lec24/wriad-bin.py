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
import pickle

data = [("Евгений онегин", "Пушкин", 200),
        ("Му-му", "Тургениев", 100)]
try:
    file1 = open('out-bin.bin', "wb")
    try:
        pickle.dump(data, file1)

    finally:
        file1.close()

except FileNotFoundError:
    print("Файл ненайден")
print("-----------------------------------------")
try:
    file1 = open('out-bin.bin', "rb")
    try:
        bs = pickle.load(file1)
        for n in range(len(bs)):
            print(bs[n])
    finally:
        file1.close()

except FileNotFoundError:
    print("Файл ненайден")