#!/usr/bin/env python
# -*- coding: utf8 -*-
import os

import wx

ID_TXT = 1
ID_EXCEL = 2
ID_ZIP = 3
ID_EXIT = 10


# VIEW_STATUS = 5


class AppFileMenu(wx.Menu):
    def __init__(self, parent):
        self.parent = parent
        super().__init__()

        open_file = self.Append(wx.ID_ANY, '&Открыть \tCtrl+O')

        # self.Append(ID_TXT, '&Открыть txt\tCtrl+T')
        # self.Append(ID_EXCEL, '&Открыть excel\tCtrl+E')
        # self.Append(ID_ZIP, '&Открыть zip\tCtrl+Z')

        # expMenu = wx.Menu()
        #
        # expMenu.Append(wx.ID_ANY, "Экспорт изображения")
        # expMenu.Append(wx.ID_ANY, "Экспорт видео")
        # expMenu.Append(wx.ID_ANY, "Экспорт данных")
        #
        # self.AppendSubMenu(expMenu, "&Экспорт")
        # self.vStatus = self.Append(VIEW_STATUS, 'Статустная строка', kind=wx.ITEM_CHECK)
        self.AppendSeparator()  # создания вкладки меню; ITEM_SEPARATOR

        exit_prog = wx.MenuItem(self, ID_EXIT, "Выход\tCtrl+Q", "Выход из приложения")
        exit_prog.SetBitmap(wx.Bitmap('image/exit16.png'))
        self.Append(exit_prog)

        self.Bind(wx.EVT_MENU, self.open_file, id=open_file.GetId())
        # self.Bind(wx.EVT_MENU, self.open_file_txt, id=ID_TXT)
        # self.Bind(wx.EVT_MENU, self.open_file_excel, id=ID_EXCEL)
        # self.Bind(wx.EVT_MENU, self.open_file_zip, id=ID_ZIP)

        self.Bind(wx.EVT_MENU, self.onQuit, id=exit_prog.GetId())

    def open_file(self, event):
        """ открывает  файл
            если файл не выбран то программа  не запускается !!!

        """
        with wx.FileDialog(self.parent, "Открыть файл", "", "",
                           "Все файлы| *.*",
                           wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
            pathname = fileDialog.GetPath()
            print(pathname)

        if pathname:
            os.startfile(pathname)
        else:
            return


    def open_file_txt(self, event):
        """ открывает найденый файл в текстовом редакторе
            если файл не выбран то программа блокнот не запускается !!!

        """

        with wx.FileDialog(self.parent, "Открыть файл", "", "",
                           "Текстовый файл (*.txt)| *.txt|"
                           "Все файлы| *.*",
                           wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
            pathname = fileDialog.GetPath()
            print(pathname)

        if pathname:
            os.startfile(pathname)
        else:
            return

    def open_file_excel(self, event):
        """ открывает найденый файл в текстовом редакторе
            если файл не выбран то программа excel не запускается !!!
        """

        with wx.FileDialog(self.parent, "Открыть файл", "", "",
                           "Книга excel (*.xlsx)| *.xlsx|"
                           "Книга excel 97-2003 (*.xls)| *.xls|"
                           "Все файлы| *.*",
                           wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
            pathname = fileDialog.GetPath()
            print(pathname)

        if pathname:
            os.startfile(pathname)
        else:
            return

    def open_file_zip(self, event):
        """ Открывает путь к файлу ZIP """

        with wx.FileDialog(self.parent, "Open", "", "",
                           "zip файлы (*.zip)| *.zip|"
                           "rar файлы (*.zip)| *.rar|"
                           "Все файлы| *.*",
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
