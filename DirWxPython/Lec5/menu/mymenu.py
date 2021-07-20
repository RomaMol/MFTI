#!/usr/bin/env python
# -*- coding: utf8 -*-

#  https://www.youtube.com/watch?v=6NCmQwVPXFU&list=PLA0M1Bcd0w8zyJOJXbvTKROHs2JJVGB6C&index=4
#  wxPython #4: контекстное меню и панель инструментов (toolbar)


import wx

from DirWxPython.Lec4.menu.contextmenu import AppContextMenu
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
        # ------------------------------------------------------------------------------
        panel = wx.Panel(self)  # задать панель для размещения  сайзера и элементов
        panel.SetBackgroundColour('#FFFFE5')
        vbox = wx.BoxSizer(wx.VERTICAL)  # задать сайзер


        #vbox.Add(panel, wx.ID_ANY, wx.EXPAND | wx.ALL, 20)
        img1 = wx.StaticBitmap(panel, wx.ID_ANY, wx.Bitmap("png/sound32-on.png"))
        img2 = wx.StaticBitmap(panel, wx.ID_ANY, wx.Bitmap("png/sound32-off.png"))

        # img1.SetPosition((10, 10)
        # img2.SetPosition((300, 40))
        vbox.Add(img1, wx.ID_ANY, wx.EXPAND)  # поместить в сайзер
        vbox.Add(img2, wx.ID_ANY, wx.EXPAND)
        panel.SetSizer(vbox)  # вывести  сайзер на экран закрепленный на панели






    def onQuit(self, event):
        self.Close()
