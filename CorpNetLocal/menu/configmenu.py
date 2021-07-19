#!/usr/bin/env python
# -*- coding: utf8 -*-
import wx

ID_HELP = 1
ID_CONF = 2
ID_PROG = 3

class AppConfigMenu(wx.Menu):

    def __init__(self, parent):
        self.parent = parent
        super().__init__()

        self.Append(ID_CONF, 'Конфигурация')
        self.Append(ID_HELP, '&Помощь\tCtrl+H')
        self.Append(ID_PROG, 'О программе')