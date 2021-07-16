#!/usr/bin/env python
# -*- coding: utf8 -*-

#  https://www.youtube.com/watch?v=Y__0Xrm0Mp0&list=PLA0M1Bcd0w8zyJOJXbvTKROHs2JJVGB6C&index=3
#  wxPython #3: создание меню и подменю - MenuBar, Menu, MenuItem, Bind, Append, AppendSeparator

# MenuBar – для создания панели меню;
# Menu – для создания вкладки меню;
# MenuItem – для создания отдельного пункта.

#               Bind(event, handler, source=None)
#           event – тип события, связанный с определенным интерфейсным объектом;
#           handler – ссылка на функцию-обработчик;
#           source – источник, генерирующий событие.
import wx

ID_EXIT = 1


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title)

        menubar = wx.MenuBar()  # создание менюбара
        fileMenu = wx.Menu()  # создания вкладки меню;

        fileMenu.Append(wx.ID_NEW, '&Новый\tCtrl+N')
        fileMenu.Append(wx.ID_OPEN, '&Открыть\tCtrl+O')
        fileMenu.Append(wx.ID_SAVE, '&Сохранить\tCtrl+S')

        item = wx.MenuItem(fileMenu, ID_EXIT, "Выход\tCtrl+Q", "Выход из приложения")
        item.SetBitmap(wx.Bitmap('menu/exit_icon_176956.png'))
        fileMenu.Append(item)
        # item = fileMenu.Append(
        #     wx.MenuItem(fileMenu, wx.ID_EXIT, "Выход\tCtrl+Q", "Выход из приложения"))  # создания отдельного пункта.

        menubar.Append(fileMenu, "&File")  # отражение вкладки меню в окне
        self.SetMenuBar(menubar)  # создание менюбара отражение панели в окне

        self.Bind(wx.EVT_MENU, self.onQuit, id=ID_EXIT)

    def onQuit(self, event):
        self.Close()
