#!/usr/bin/env python
# -*- coding: utf8 -*-


#  https://youtu.be/DdHMnHeX5rY
#  wxPython #7: механизм обработки событий - Bind, Unbind

import wx

from DirWxPython.Lec7.menu.sizer import MyFrame

if __name__ == '__main__':
    app = wx.App()  # инициируем запуска приложения
    frame = MyFrame(None, title="Hello world", )  # главное окно программы
    frame.Center()  # разместить по центру
    frame.Show()  # показать на экране
    app.MainLoop()  # Главный цикл запуска приложения
