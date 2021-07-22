#!/usr/bin/env python
# -*- coding: utf8 -*-
import os

import wx


class AppFileMenu(wx.Menu):
    def __init__(self, parent):
        self.parent = parent
        super().__init__()

        open_file = self.Append(wx.ID_ANY, '&Открыть \tCtrl+O')

        self.AppendSeparator()  # создания вкладки меню; ITEM_SEPARATOR

        exit_pro = wx.MenuItem(self, wx.ID_ANY, "Выход\tCtrl+Q", "Выход из приложения")
        exit_pro.SetBitmap(wx.Bitmap('image/exit16.png'))
        self.Append(exit_pro)

        self.Bind(wx.EVT_MENU, self.open_file, id=open_file.GetId())
        self.Bind(wx.EVT_MENU, self.onQuit, id=exit_pro.GetId())

    def open_file(self, event):
        """ открывает  файл
            если файл не выбран то программа  не запускается !!!

        """
        with wx.FileDialog(self.parent, "Открыть файл", "", "",
                           "Все файлы| *.*|"
                           "Текстовый файл (*.txt)| *.txt|"
                           "Книга excel (*.xlsx)| *.xlsx|"
                           "Книга excel 97-2003 (*.xls)| *.xls|"
                           "zip файлы (*.zip)| *.zip|"
                           "rar файлы (*.rar)| *.rar",
                           wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
            pathname = fileDialog.GetPath()
            print(pathname)

        if pathname:
            os.startfile(pathname)
        else:
            return

    def onQuit(self, event):
        self.parent.Close()
