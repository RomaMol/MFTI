#!/usr/bin/env python
# -*- coding: utf8 -*-

#  https://youtu.be/dSBY6F8qsmM
#  wxPython #8: примеры событий, назначение id виджетам

import wx

from DirWxPython.Lec8.menu.bingID import MyFrame

if __name__ == '__main__':
    app = wx.App()  # инициируем запуска приложения
    frame = MyFrame(None, title="Hello world", )  # главное окно программы
    frame.Center()  # разместить по центру
    frame.Show()  # показать на экране
    app.MainLoop()  # Главный цикл запуска приложения
