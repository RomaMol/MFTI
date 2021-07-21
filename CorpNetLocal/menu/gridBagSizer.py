#!/usr/bin/env python
# -*- coding: utf8 -*-

#  https://youtu.be/7ehPJFL90mc
#  wxPython #6: сайзеры - GridSizer, FlexGridSizer, GridBagSizer

# GridBagSizer(vgap, hgap) -- расстояния между ячейками в пикселах
#
# Add(self, item, pos, span=wx.DefaultSpan, flag=0, border=0, userData=None)
# item = wx.StaticText(panel, label="Email:")
# pos=(row, col)
#
import wx


ID_EXIT = 1


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title)

        # -------------------------calculate ----------------------------------------------------
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        gr = wx.GridBagSizer(5, 5)
        text = wx.StaticText(panel, label="Email:")
        tc = wx.TextCtrl(panel)
        button1 = wx.Button(panel, label="Восстановить", size=(120, 28))
        button2 = wx.Button(panel, label="Отмена", size=(90, 28))


        gr.Add(text, pos=(0, 0), flag=wx.TOP | wx.LEFT | wx.BOTTOM, border=5)
        gr.Add(tc, pos=(1, 0), span=(1, 5), flag=wx.EXPAND | wx.LEFT | wx.RIGHT, border=5)
        gr.Add(button1, pos=(3, 3))
        gr.Add(button2, pos=(3, 4), flag=wx.RIGHT | wx.BOTTOM, border=10)

        gr.AddGrowableCol(1)
        gr.AddGrowableRow(2)

        vbox.Add(gr, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        panel.SetSizer(vbox)

    def onQuit(self, event):
        self.Close()

if __name__ == '__main__':

    app = wx.App()  # инициируем запуска приложения
    frame = MyFrame(None, title="Hello world", )  # главное окно программы
    frame.Center()  # разместить по центру
    frame.Show()  # показать на экране
    app.MainLoop()  # Главный цикл запуска приложения