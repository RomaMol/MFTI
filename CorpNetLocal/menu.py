#!/usr/bin/env python
# -*- coding: utf8 -*-

import wx

from CorpNetLocal.menu.configtxt import the_first_run
from CorpNetLocal.menu.progmenubar import MyFrame

CorpNet = wx.App()
window = MyFrame(None, title="CorpNet-Local", )
#the_first_run()
window.Center()
window.Show()

CorpNet.MainLoop()
