#!/usr/bin/env python
# -*- coding: utf8 -*-
import wx


from CorpNetLocal.configmenu.menuconfig1 import MyDialog


class AppConfigMenu(wx.Menu):

    def __init__(self, parent):
        self.parent = parent
        super().__init__()

        config = self.Append(wx.ID_ANY, 'Конфигурация')
        helps = self.Append(wx.ID_ANY, '&Помощь\tCtrl+H')
        o_pro = self.Append(wx.ID_ANY, 'О программе')

        self.Bind(wx.EVT_MENU, self.onDialog, id=config.GetId())
        self.Bind(wx.EVT_MENU, self.help, id=helps.GetId())
        self.Bind(wx.EVT_MENU, self.o_pro, id=o_pro.GetId())

    def onDialog(self, e):
        dlg = MyDialog(self.parent, title="Конфигурация")
        dlg.Center()
        dlg.ShowModal()
        dlg.Destroy()

    def help(self, event):
        print("list help")
        pass

    def o_pro(self, event):
        print("list o programme")
        pass
