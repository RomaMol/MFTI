#!/usr/bin/env python
# -*- coding: utf8 -*-

#  https://youtu.be/dSBY6F8qsmM
#  wxPython #8: примеры событий, назначение id виджетам


import wx

ID_EXIT = 1


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title)

        # -------------------------Bind, Unbind ----------------------------------------------------




    def onButton1(self, event):
        print("Нажатие на 1 кнопку мыши")

    def onButton2(self, event):
        print("Нажатие на 2 кнопку мыши")

    def onButton3(self, event):
        print("Нажатие на 3 кнопку мыши")

    def onButton4(self, event):
        print("Нажатие на 4 кнопку мыши")



if __name__ == '__main__':
    app = wx.App()  # инициируем запуска приложения
    frame = MyFrame(None, title="Hello world", )  # главное окно программы
    frame.Center()  # разместить по центру
    frame.Show()  # показать на экране
    app.MainLoop()  # Главный цикл запуска приложения
