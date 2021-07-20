#!/usr/bin/env python
# -*- coding: utf8 -*-

#  https://youtu.be/4tkvthAC3k8
#  wxPython #5: схемы (layout) размещения виджетов, BoxSizer


import wx

from DirWxPython.Lec4.menu.filemenu import AppFileMenu
from DirWxPython.Lec4.menu.viewmenu import AppViewMenu

ID_EXIT = 1


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title)

        menubar = wx.MenuBar()  # создание менюбара
        fileMenu = AppFileMenu(self)  # создания вкладки меню fileMenu ; ITEM_NORMAL
        viewMenu = AppViewMenu(self)  # создания вкладки меню ViewMenu ; ITEM_NORMAL
        menubar.Append(fileMenu, "&File")
        menubar.Append(viewMenu, "&Вид")
        self.SetMenuBar(menubar)

        # --------------создание панели для размещения элементов----------------------------
        panel = wx.Panel(self)  # задать панель для размещения  сайзера и элементов
        # ------------замена шрифта на панели------------------------------------------------
        font = wx.SystemSettings.GetFont(wx.SYS_DEFAULT_GUI_FONT)
        font.SetPointSize(12)
        panel.SetFont(font)

        verbox = wx.BoxSizer(wx.VERTICAL)  # вертикальное расположение боксов

        # --------------------первая группа элементов ----------------------------------
        h1 = wx.BoxSizer(wx.HORIZONTAL)
        st1 = wx.StaticText(panel, label='Путь к файлу:')
        tc = wx.TextCtrl(panel)

        h1.Add(st1, flag=wx.RIGHT, border=8)
        h1.Add(tc, proportion=1)

        verbox.Add(h1, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)
        # ---------------------вторая группа элементов---------------------------------
        st2 = wx.StaticText(panel, label='Содержимое файла')
        verbox.Add(st2, flag=wx.EXPAND | wx.ALL, border=10)
        # ---------------------третья  группа элементов---------------------------------
        tc2 = wx.TextCtrl(panel, style=wx.TE_MULTILINE)
        verbox.Add(tc2, proportion=1, flag=wx.LEFT | wx.RIGHT | wx.BOTTOM | wx.EXPAND, border=10)
        # ---------------------4   группа элементов---------------------------------
        btnOk = wx.Button(panel, label='Да', size=(70, 30))
        btnCn = wx.Button(panel, label='Отмена', size=(70, 30))

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2.Add(btnOk, flag=wx.LEFT, border=10)
        hbox2.Add(btnCn, flag=wx.LEFT, border=10)
        verbox.Add(hbox2, flag=wx.ALIGN_RIGHT | wx.BOTTOM | wx.RIGHT, border=10)

        # ---------------привязка verbox  к панели ------------------------------
        panel.SetSizer(verbox)  # вертикальное расположение боксов отражение на экране

    def onQuit(self, event):
        self.Close()
