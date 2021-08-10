#!/usr/bin/env python
# -*- coding: utf8 -*-

import wx

from CorpNetLocal.configmenu.configmenu import AppConfigMenu
from CorpNetLocal.menu.contextmenu import AppContextMenu
from CorpNetLocal.configmenu.filemenu import AppFileMenu

boottomsize = (90, 30)
bottomborder = 20


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title)
        # -----------иконка слева от названия программы----------------
        ico = wx.Icon('image/253.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(wx.Icon(ico))
        # -----------верхнее меню и Контекстное меню----------------
        menubar = wx.MenuBar()  # создание менюбара
        filemenu = AppFileMenu(self)
        configmenu = AppConfigMenu(self)
        self.ctx = AppContextMenu(self)
        menubar.Append(filemenu, "&Файл")
        menubar.Append(configmenu, "&Настройка")
        self.SetMenuBar(menubar)

        # -----------бокс  меню----------------
        panel = wx.Panel(self)

        font = wx.SystemSettings.GetFont(wx.SYS_DEFAULT_GUI_FONT)
        font.SetPointSize(12)
        panel.SetFont(font)

        verbox = wx.BoxSizer(wx.VERTICAL)  # вертикальное расположение боксов

        # -------------------- 1 ----------------------
        h1 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(panel, label='Введите IP адрес')
        h1.Add(st1, flag=wx.CENTRE | wx.BOTTOM, border=0)
        verbox.Add(h1, flag=wx.CENTRE | wx.BOTTOM, border=10)
        # -------------------- 2 ----------------------
        h2 = wx.BoxSizer(wx.HORIZONTAL)
        tc = wx.TextCtrl(panel, size=(220, 30))
        h2.Add(tc, flag=wx.CENTER, border=8)
        verbox.Add(h2, flag=wx.CENTRE | wx.BOTTOM, border=10)
        # -------------------- 3----------------------

        h3 = wx.BoxSizer(wx.HORIZONTAL)

        btnFoto = wx.Button(panel, label='ФОТО', size=boottomsize)
        btnSerch = wx.Button(panel, label='ПОИСК', size=boottomsize)
        h3.Add(btnFoto, flag=wx.RIGHT, border=bottomborder)
        h3.Add(btnSerch, flag=wx.LEFT, border=bottomborder)

        verbox.Add(h3, flag=wx.CENTRE | wx.BOTTOM | wx.CENTRE, border=10)
        # ---------------------- 4 ------------------------------

        h4 = wx.BoxSizer(wx.HORIZONTAL)

        btnSSH = wx.Button(panel, label='PuTTY SSH', size=boottomsize)
        btnHTTP = wx.Button(panel, label='HTTP', size=boottomsize)
        h4.Add(btnSSH, flag=wx.RIGHT, border=bottomborder)
        h4.Add(btnHTTP, flag=wx.LEFT, border=bottomborder)

        verbox.Add(h4, flag=wx.CENTRE | wx.BOTTOM | wx.CENTRE, border=10)
        # ---------------------- 5 ------------------------------

        h5 = wx.BoxSizer(wx.HORIZONTAL)

        btnTelnet = wx.Button(panel, label='Telnet', size=boottomsize)
        btnHTTPS = wx.Button(panel, label='HTTPS', size=boottomsize)
        h5.Add(btnTelnet, flag=wx.RIGHT, border=bottomborder)
        h5.Add(btnHTTPS, flag=wx.LEFT, border=bottomborder)

        verbox.Add(h5, flag=wx.CENTRE | wx.BOTTOM | wx.CENTRE, border=10)

        # ---------------------- 6 ------------------------------

        h6 = wx.BoxSizer(wx.HORIZONTAL)

        btnPing = wx.Button(panel, label='PING!!!', size=boottomsize)
        h6.Add(btnPing, flag=wx.CENTER, border=bottomborder)

        verbox.Add(h6, flag=wx.CENTRE | wx.BOTTOM | wx.CENTRE, border=10)

        # --------------------------7------------------------------------
        tc7 = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        verbox.Add(tc7, proportion=1, flag=wx.LEFT | wx.RIGHT | wx.BOTTOM | wx.EXPAND, border=10)
        # ----------------------------------------------------------------
        panel.SetSizer(verbox)  # вертикальное расположение боксов отражение на экране

        self.Bind(wx.EVT_RIGHT_DOWN, self.OnRightDown)  # подключение Контекстное меню

    def OnRightDown(self, event):
        self.PopupMenu(self.ctx, event.GetPosition())
        print(event.GetPosition())


if __name__ == '__main__':
    CorpNet = wx.App()
    window = MyFrame(None, title="CorpNet-Local", )
    window.Center()
    window.Show()
    CorpNet.MainLoop()
