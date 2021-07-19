#!/usr/bin/env python
# -*- coding: utf8 -*-

#  https://www.youtube.com/watch?v=6NCmQwVPXFU&list=PLA0M1Bcd0w8zyJOJXbvTKROHs2JJVGB6C&index=4
#  wxPython #4: контекстное меню и панель инструментов (toolbar)

import wx

VIEW_STATUS = 2
VIEW_RGB = 3
VIEW_SRGB = 4

class AppViewMenu(wx.Menu):
    def __init__(self, parent):
        self.parent = parent
        super().__init__()

        self.vStatus = self.Append(VIEW_STATUS, 'Статустная строка', kind=wx.ITEM_CHECK)
        self.vRgb = self.Append(VIEW_RGB, 'Тип RGB', 'Тип RGB', kind=wx.ITEM_RADIO)
        self.vSrgb = self.Append(VIEW_SRGB, 'Тип sRGB', 'Тип sRGB', kind=wx.ITEM_RADIO)

        self.Bind(wx.EVT_MENU, self.onStatus, id=VIEW_STATUS)
        self.Bind(wx.EVT_MENU, self.onImageType, id=VIEW_RGB)
        self.Bind(wx.EVT_MENU, self.onImageType, id=VIEW_SRGB)

    def onStatus(self, event):
        if self.vStatus.IsChecked():
            print("Показать статусную строку")
        else:
            print("Скрыть статусную строку")

    def onImageType(self, event):
        if self.vRgb.IsChecked():
            print("Режим RGB")
        elif self.vSrgb.IsChecked():
            print("Режим sRGB")