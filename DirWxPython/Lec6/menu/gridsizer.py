#!/usr/bin/env python
# -*- coding: utf8 -*-

#  https://youtu.be/7ehPJFL90mc
#  wxPython #6: сайзеры - GridSizer, FlexGridSizer, GridBagSizer

# wx.GridSizer(rows=1, cols=0, vgap=0, hgap=0)
#
# rows – число строк (отсчет начинается с 1);
# cols – число столбцов (отсчет идет с 0);
# vgap – интервал между ячейками по вертикали;
# hgap – интервал между ячейками по горизонтали.
import wx


ID_EXIT = 1


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title)

        # -------------------------calculate ----------------------------------------------------
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)
        tc = wx.TextCtrl(panel)
        vbox.Add(tc, flag=wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, border=10)
        gbox = wx.GridSizer(5, 4, 5, 5)

        gbox.AddMany([(wx.Button(panel, label='Cls'), 0, wx.EXPAND),
                      (wx.Button(panel, label='Bck'), 0, wx.EXPAND),
                      (wx.StaticText(panel), wx.EXPAND),
                      (wx.Button(panel, label='Close'), 0, wx.EXPAND),
                      (wx.Button(panel, label='7'), 0, wx.EXPAND),
                      (wx.Button(panel, label='8'), 0, wx.EXPAND),
                      (wx.Button(panel, label='9'), 0, wx.EXPAND),
                      (wx.Button(panel, label='/'), 0, wx.EXPAND),
                      (wx.Button(panel, label='4'), 0, wx.EXPAND),
                      (wx.Button(panel, label='5'), 0, wx.EXPAND),
                      (wx.Button(panel, label='6'), 0, wx.EXPAND),
                      (wx.Button(panel, label='*'), 0, wx.EXPAND),
                      (wx.Button(panel, label='1'), 0, wx.EXPAND),
                      (wx.Button(panel, label='2'), 0, wx.EXPAND),
                      (wx.Button(panel, label='3'), 0, wx.EXPAND),
                      (wx.Button(panel, label='-'), 0, wx.EXPAND),
                      (wx.Button(panel, label='0'), 0, wx.EXPAND),
                      (wx.Button(panel, label='.'), 0, wx.EXPAND),
                      (wx.Button(panel, label='='), 0, wx.EXPAND),
                      (wx.Button(panel, label='+'), 0, wx.EXPAND)])

        vbox.Add(gbox, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        panel.SetSizer(vbox)

    def onQuit(self, event):
        self.Close()

if __name__ == '__main__':

    app = wx.App()  # инициируем запуска приложения
    frame = MyFrame(None, title="Hello world", )  # главное окно программы
    frame.Center()  # разместить по центру
    frame.Show()  # показать на экране
    app.MainLoop()  # Главный цикл запуска приложения