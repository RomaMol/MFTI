#!/usr/bin/env python
# -*- coding: utf8 -*-

#  https://youtu.be/7ehPJFL90mc
#  wxPython #6: сайзеры - GridSizer, FlexGridSizer, GridBagSizer

# Для начала создадим такой сайзер с 4 строками, 2 столбцами и расстояниями между ячейками 10 пикселей:
#
# fb = wx.FlexGridSizer(4, 2, 10, 10)
import wx

ID_EXIT = 1


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title)

        # -------------------------calculate ----------------------------------------------------
        panel = wx.Panel(self)
        hbox = wx.BoxSizer()

        fb = wx.FlexGridSizer(4, 2, 10, 10)
        fb.AddMany([(wx.StaticText(panel, label="Ф.И.О.:")),
                    (wx.TextCtrl(panel), wx.ID_ANY, wx.EXPAND),
                    (wx.StaticText(panel, label="email:")),
                    (wx.TextCtrl(panel), wx.ID_ANY, wx.EXPAND),
                    (wx.StaticText(panel, label="Адрес:")),
                    (wx.TextCtrl(panel), wx.ID_ANY, wx.EXPAND),
                    (wx.StaticText(panel, label="О себе:")),
                    (wx.TextCtrl(panel, style=wx.NB_MULTILINE), wx.ID_ANY, wx.EXPAND)
                    ])
        # AddGrowableCol(self, col, proportion=0) proportion=1 для второго столбца (col=1)
        # AddGrowableRow(self, row, proportion=0) и для row=3 укажем proportion=1:
        fb.AddGrowableCol(1, 1)
        fb.AddGrowableRow(3, 1)

        hbox.Add(fb, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        panel.SetSizer(hbox)

    def onQuit(self, event):
        self.Close()


if __name__ == '__main__':
    app = wx.App()  # инициируем запуска приложения
    frame = MyFrame(None, title="Hello world", )  # главное окно программы
    frame.Center()  # разместить по центру
    frame.Show()  # показать на экране
    app.MainLoop()  # Главный цикл запуска приложения
