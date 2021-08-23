#!/usr/bin/env python
# -*- coding: utf8 -*-

import wx
from wx import ID_ANY

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

        box = wx.BoxSizer(wx.VERTICAL)  # вертикальное расположение боксов

        # -------------------- 1 ----------------------
        h1 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(panel, label='Введите IP адрес')
        h1.Add(st1, flag=wx.CENTRE | wx.BOTTOM, border=0)
        box.Add(h1, flag=wx.CENTRE | wx.BOTTOM, border=10)
        # -------------------- 2 ----------------------
        h2 = wx.BoxSizer(wx.HORIZONTAL)
        self.tc = wx.TextCtrl(panel, id=ID_ANY, size=(220, 30))

        h2.Add(self.tc, flag=wx.CENTER, border=8)
        box.Add(h2, flag=wx.CENTRE | wx.BOTTOM, border=10)
        # # -------------------- 3----------------------
        h3 = wx.BoxSizer(wx.HORIZONTAL)
        gr = wx.GridBagSizer(5, 5)
        button1 = wx.Button(panel, label='ФОТО', size=boottomsize)
        button2 = wx.Button(panel, label='ПОИСК', size=boottomsize)
        button3 = wx.Button(panel, label='PuTTY SSH', size=boottomsize)
        button4 = wx.Button(panel, label='HTTP', size=boottomsize)
        button5 = wx.Button(panel, label='Telnet', size=boottomsize)
        button6 = wx.Button(panel, label='HTTPS', size=boottomsize)
        button7 = wx.Button(panel, label='PING!!!', size=boottomsize)

        gr.Add(button1, pos=(0, 0))
        gr.Add(button2, pos=(0, 2))
        gr.Add(button3, pos=(1, 0))
        gr.Add(button4, pos=(1, 2))
        gr.Add(button5, pos=(2, 0))
        gr.Add(button6, pos=(2, 2))
        gr.Add(button7, pos=(3, 1))

        h3.Add(gr, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        box.Add(h3, flag=wx.CENTRE | wx.BOTTOM | wx.CENTRE, border=10)

        # --------------------------7------------------------------------
        tc7 = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        box.Add(tc7, proportion=1, flag=wx.LEFT | wx.RIGHT | wx.BOTTOM | wx.EXPAND, border=10)
        # ----------------------------------------------------------------

        panel.SetSizer(box)  # вертикальное расположение боксов отражение на экране

        panel.Bind(wx.EVT_RIGHT_DOWN, self.OnRightDown)  # подключение Контекстное меню
        self.Bind(wx.EVT_BUTTON, self.button2, id=button2.GetId())
        self.Bind(wx.EVT_BUTTON, self.button7, id=button7.GetId())

    def OnRightDown(self, event):
        """Нажатие на правую кнопку мыши"""
        self.PopupMenu(self.ctx, event.GetPosition())


    def button2(self, event):
        """Нажатие на  кнопку ПОИСК"""

        tc1 = self.tc.GetValue()

        print("ПОИСК",  tc1)

    def button7(self, event):
        """Нажатие на  кнопку PING!!!"""
        tc1 = self.tc.GetValue()

        print("PING", tc1)

if __name__ == '__main__':
    CorpNet = wx.App()
    window = MyFrame(None, title="CorpNet-Local", )
    window.Center()
    window.Show()
    CorpNet.MainLoop()
