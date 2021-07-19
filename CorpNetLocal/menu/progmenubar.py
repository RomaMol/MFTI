#!/usr/bin/env python
# -*- coding: utf8 -*-

import wx

from CorpNetLocal.menu.configmenu import AppConfigMenu
from CorpNetLocal.menu.filemenu import AppFileMenu


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title)

        menubar = wx.MenuBar()  # создание менюбара

        filemenu = AppFileMenu(self)
        configmenu = AppConfigMenu(self)

        menubar.Append(filemenu, "&Файл")
        menubar.Append(configmenu, "&Настройка")
        self.SetMenuBar(menubar)

