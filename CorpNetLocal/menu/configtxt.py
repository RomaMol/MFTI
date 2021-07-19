#!/usr/bin/env python
# -*- coding: utf8 -*-

import os

one_ini = "\n\n\nN, №, N п.п, №п.п, № п.п, №п/п, № п/п\n\n\n"
too_ini = "name1\nlogin1\nip_address1\npassword1\n" \
          "name2\nlogin2\nip_address2\npassword2\n"
conf_file_ini = ['config.ini', 'config2.ini']
ini = [one_ini, too_ini]


def the_first_run():
    """ первый запуск программы проверка файла конфиг если нет создание"""

    one = os.path.exists(conf_file_ini[0])
    too = os.path.exists(conf_file_ini[1])
    if one or too is True:
        return

    for file in conf_file_ini:
        index_conf = conf_file_ini.index(file)
        data = ini[index_conf]
        file = open(file, "w")
        file.write(data)
        file.close()
