#!/usr/bin/env python
# -*- coding: utf8 -*-

import wx

from CorpNetLocal.menu.configtxt import the_first_run
from CorpNetLocal.menu.progmenu import MyFrame

if __name__ == '__main__':
    CorpNet = wx.App()
    window = MyFrame(None, title="CorpNet-Local", )
    window.Center()
    window.Show()
    CorpNet.MainLoop()
