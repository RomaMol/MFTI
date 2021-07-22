#!/usr/bin/env python
# -*- coding: utf8 -*-

import os

one_ini = "\n\n\nN, №, N п.п, №п.п, № п.п, №п/п, № п/п\n\n\n"

conf_file_ini = ['config.ini']
ini = [one_ini]


def the_first_run():
    """ первый запуск программы проверка файла конфиг если нет создание"""

    one = os.path.exists(conf_file_ini[0])

    if one  is True:
        return

    for file in conf_file_ini:
        index_conf = conf_file_ini.index(file)
        data = ini[index_conf]
        file = open(file, "w")
        file.write(data)
        file.close()
