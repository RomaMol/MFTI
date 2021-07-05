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

try:
    file1 = open('out.txt', "w", encoding="utf-8")
    try:
        file1.write("Hello asferger\n")
        file1.write("Hello asferger\n")
        file1.write("Hello asferger\n")
    finally:
        file1.close()

except FileNotFoundError:
    print("Файл ненайден")
print("-----------------------------------------")

try:
    file1 = open('out.txt', "a", encoding="utf-8")
    try:
        file1.write("Hello \n")
        file1.write("Hello \n")
        file1.write("Hello \n")
    finally:
        file1.close()

except FileNotFoundError:
    print("Файл ненайден")
print("-----------------------------------------")

try:
    file1 = open('out1.txt', "a+", encoding="utf-8")
    try:
        file1.write("Hello \n")
        file1.write("Hello \n")
        file1.write("Hello \n")
        file1.seek(0)
        print(file1.readlines())
    finally:
        file1.close()

except FileNotFoundError:
    print("Файл ненайден")
print("-----------------------------------------")