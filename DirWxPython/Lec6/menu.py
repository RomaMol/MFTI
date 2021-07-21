#!/usr/bin/env python
# -*- coding: utf8 -*-


#  https://youtu.be/7ehPJFL90mc
#  wxPython #6: сайзеры - GridSizer, FlexGridSizer, GridBagSizer

import wx

from DirWxPython.Lec6.menu.gridsizer import MyFrame

if __name__ == '__main__':
    app = wx.App()  # инициируем запуска приложения
    frame = MyFrame(None, title="Hello world", )  # главное окно программы
    frame.Center()  # разместить по центру
    frame.Show()  # показать на экране
    app.MainLoop()  # Главный цикл запуска приложения
