#!/usr/bin/env python
# -*- coding: utf8 -*-

#  https://www.youtube.com/watch?v=6NCmQwVPXFU&list=PLA0M1Bcd0w8zyJOJXbvTKROHs2JJVGB6C&index=4
#  wxPython #4: контекстное меню и панель инструментов (toolbar)

import wx

ID_EXIT = 1


class AppFileMenu(wx.Menu):
    def __init__(self, parent):
        self.parent = parent
        super().__init__()

        self.Append(wx.ID_NEW, '&Новый\tCtrl+N')
        self.Append(wx.ID_OPEN, '&Открыть\tCtrl+O')
        self.Append(wx.ID_SAVE, '&Сохранить\tCtrl+S')

        expMenu = wx.Menu()

        expMenu.Append(wx.ID_ANY, "Экспорт изображения")
        expMenu.Append(wx.ID_ANY, "Экспорт видео")
        expMenu.Append(wx.ID_ANY, "Экспорт данных")

        self.AppendSubMenu(expMenu, "&Экспорт")

        self.AppendSeparator()  # создания вкладки меню; ITEM_SEPARATOR

        exit_prog = wx.MenuItem(self, ID_EXIT, "Выход\tCtrl+Q", "Выход из приложения")
        exit_prog.SetBitmap(wx.Bitmap('png/exit16.png'))
        self.Append(exit_prog)

        self.Bind(wx.EVT_MENU, self.onQuit, id=ID_EXIT)

    def onQuit(self, event):
        self.parent.Close()
