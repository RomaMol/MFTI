#!/usr/bin/env python
# -*- coding: utf8 -*-
import wx

from CorpNetLocal.configmenu.menuconfig1 import MyFrame1


class AppConfigMenu(wx.Menu):

    def __init__(self, parent):
        self.parent = parent
        super().__init__()

        config = self.Append(wx.ID_ANY, 'Конфигурация')
        helps = self.Append(wx.ID_ANY, '&Помощь\tCtrl+H')
        o_pro = self.Append(wx.ID_ANY, 'О программе')

        self.Bind(wx.EVT_MENU, self.config, id=config.GetId())
        self.Bind(wx.EVT_MENU, self.help, id=helps.GetId())
        self.Bind(wx.EVT_MENU, self.o_pro, id=o_pro.GetId())

    def config(self, event):
        print("list config")
        menuconfig1 = wx.App()
        window1 = MyFrame1(None, title="Настройка", )
        window1.Center()
        #window1.ShowModal()
        menuconfig1.MainLoop()



    def help(self, event):
        print("list help")
        pass

    def o_pro(self, event):
        print("list o programme")
        pass
