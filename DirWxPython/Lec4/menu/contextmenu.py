#!/usr/bin/env python
# -*- coding: utf8 -*-

#  https://www.youtube.com/watch?v=6NCmQwVPXFU&list=PLA0M1Bcd0w8zyJOJXbvTKROHs2JJVGB6C&index=4
#  wxPython #4: контекстное меню и панель инструментов (toolbar)

import wx


class AppContextMenu(wx.Menu):
    def __init__(self, parent):
        self.parent = parent
        super().__init__()


        it_min = self.Append(wx.ID_ANY, "Минимизировать")
        it_max = self.Append(wx.ID_ANY, "Распахнуть")
        self.Bind(wx.EVT_MENU, self.onMinimize, it_min)
        self.Bind(wx.EVT_MENU, self.onMaximize, it_max)

    def onMinimize(self, event):
        self.parent.Iconize()

    def onMaximize(self, event):
        self.parent.Maximize()
