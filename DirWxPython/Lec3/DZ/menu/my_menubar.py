#!/usr/bin/env python
# -*- coding: utf8 -*-

import wx

ID_EXIT = 1
ID_TXT = 2
ID_EXCEL = 3
ID_ZIP = 4
VIEW_STATUS = 5
ID_HELP = 6
ID_CONF = 7
ID_PROG = 8


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title)

        menubar = wx.MenuBar()  # создание менюбара

        fileMenu = wx.Menu()
        configMenu = wx.Menu()

        fileMenu.Append(ID_TXT, '&Открыть txt\tCtrl+T')
        fileMenu.Append(ID_EXCEL, '&Открыть excel\tCtrl+E')
        fileMenu.Append(ID_ZIP, '&Открыть zip\tCtrl+Z')

        self.vStatus = fileMenu.Append(VIEW_STATUS, 'Статустная строка', kind=wx.ITEM_CHECK)
        fileMenu.AppendSeparator()  # создания вкладки меню; ITEM_SEPARATOR

        exit_prog = wx.MenuItem(fileMenu, ID_EXIT, "Выход\tCtrl+Q", "Выход из приложения")
        exit_prog.SetBitmap(wx.Bitmap('image/exit16.png'))
        fileMenu.Append(exit_prog)

        configMenu.Append(ID_CONF, 'Конфигурация')
        configMenu.Append(ID_HELP, '&Помощь\tCtrl+H')
        configMenu.Append(ID_PROG, 'О программе')

        menubar.Append(fileMenu, "&File")  # отражение вкладки меню в окне
        menubar.Append(configMenu, "&Настройка")
        self.SetMenuBar(menubar)  # создание менюбара отражение панели в окне


        self.Bind(wx.EVT_MENU, self.onStatus, id=VIEW_STATUS)
        self.Bind(wx.EVT_MENU, self.onQuit, id=ID_EXIT)

    def onQuit(self, event):
        self.Close()

    def onStatus(self, event):
        if self.vStatus.IsChecked():
            print("Показать статусную строку")
        else:
            print("Скрыть статусную строку")
