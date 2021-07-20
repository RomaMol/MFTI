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

        self.ctx = AppContextMenu(self)

        # toolbar = self.CreateToolBar()
        # toolbar = self.CreateToolBar(wx.TB_RIGHT)
        # toolbar = self.CreateToolBar(wx.TB_LEFT)
        toolbar = self.CreateToolBar(wx.TB_BOTTOM)

        br_quit = toolbar.AddTool(wx.ID_ANY, "Выход", wx.Bitmap("png/exit32.png"))
        toolbar.AddSeparator()
        br_undo = toolbar.AddTool(wx.ID_UNDO, "", wx.Bitmap("png/undo32.png"))


        br_redo = toolbar.AddTool(wx.ID_REDO, "", wx.Bitmap("png/redo32.png"))
        toolbar.EnableTool(wx.ID_REDO, False)
        #toolbar.EnableTool(wx.ID_REDO, True)
        toolbar.AddSeparator()

        toolbar.AddCheckTool(wx.ID_ANY, "", wx.Bitmap("png/sound32-on.png"))
        toolbar.AddRadioTool(wx.ID_ANY, "", wx.Bitmap("png/sound32-on.png"))
        toolbar.AddRadioTool(wx.ID_ANY, "", wx.Bitmap("png/sound32-off.png"))
        toolbar.Realize()

        menubar.Append(fileMenu, "&File")
        menubar.Append(viewMenu, "&Вид")
        self.SetMenuBar(menubar)

        self.Bind(wx.EVT_RIGHT_DOWN, self.OnRightDown)  # подключение Контекстное меню
        self.Bind(wx.EVT_TOOL, self.onQuit, br_quit)

    def OnRightDown(self, event):
        self.PopupMenu(self.ctx, event.GetPosition())

    def onQuit(self, event):
        self.Close()