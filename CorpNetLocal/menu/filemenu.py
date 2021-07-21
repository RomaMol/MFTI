#!/usr/bin/env python
# -*- coding: utf8 -*-
import os
import subprocess

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

        self.Append(ID_TXT, '&Открыть txt\tCtrl+T')
        self.Append(ID_EXCEL, '&Открыть excel\tCtrl+E')
        self.Append(ID_ZIP, '&Открыть zip\tCtrl+Z')

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

        self.Bind(wx.EVT_MENU, self.open_file_txt, id=ID_TXT)
        self.Bind(wx.EVT_MENU, self.open_file_excel, id=ID_EXCEL)
        self.Bind(wx.EVT_MENU, self.open_file_zip, id=ID_ZIP)

        self.Bind(wx.EVT_MENU, self.onQuit, id=ID_EXIT)

    def open_file_txt(self, event):
        """ открывает найденый файл в текстовом редакторе
            если файл не выбран то программа блокнот не запускается !!!

        """
        frame = wx.Frame(None, -1, 'notepad.exe')
        frame.SetDimensions(0, 0, 200, 50)

        openFileDialog = wx.FileDialog(frame, "Open", "", "",
                                       "text files (*.txt)|*.txt |all files| *.*",
                                       wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

        openFileDialog.ShowModal()
        filename = openFileDialog.GetPath()
        print(openFileDialog.GetPath())
        openFileDialog.Destroy()

        if filename:
            subprocess.Popen("notepad.exe " + filename, shell=True)
        else:
            return

    def open_file_excel(self, event):
        """ открывает найденый файл в текстовом редакторе
            если файл не выбран то программа excel не запускается !!!
        """

        frame = wx.Frame(None, -1, 'excel.exe')
        frame.SetDimensions(0, 0, 200, 50)

        openFileDialog = wx.FileDialog(frame, "Open", "", "",
                                       "Книга excel (*.xlsx)| *.xlsx|"
                                       "Книга excel 97-2003 | *.xls|"
                                       "all files| *.*",
                                       wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

        openFileDialog.ShowModal()
        filename = openFileDialog.GetPath()
        print(openFileDialog.GetPath())
        openFileDialog.Destroy()


        if filename:
            os.startfile(filename)
        else:
            return

    def open_file_zip(self, event):
        pass
    def onQuit(self, event):
        self.parent.Close()
