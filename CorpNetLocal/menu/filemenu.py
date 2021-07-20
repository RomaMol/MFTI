#!/usr/bin/env python
# -*- coding: utf8 -*-
import subprocess
from tkinter import filedialog

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

        self.Bind(wx.EVT_MENU, self.menu_up_open_file_txt, id=ID_TXT)

        self.Bind(wx.EVT_MENU, self.onQuit, id=ID_EXIT)

    def menu_up_open_file_txt(self, event):
        """ открывает найденый файл в текстовом редакторе
            если файл не выбран то программа блокнот не запускается !!!

        """
        filename = filedialog.askopenfilename(initialdir=" ",
                                              title="Открыть файл",
                                              filetypes=(("txt files", "*.txt"), ("all files", "*.*"),
                                                         ("py files", "*.py")))
        if filename:
            subprocess.Popen("notepad.exe " + filename, shell=True)
        else:
            return

    def onQuit(self, event):
        self.parent.Close()


