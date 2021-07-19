#!/usr/bin/env python
# -*- coding: utf8 -*-

import wx

from DirWxPython.Lec3.DZ.menu.my_menubar import MyFrame

CorpNet = wx.App()
window = MyFrame(None, title="CorpNet-Local", )

window.Center()
window.Show()

CorpNet.MainLoop()
