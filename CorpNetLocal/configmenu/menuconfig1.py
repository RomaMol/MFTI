#!/usr/bin/env python
# -*- coding: utf8 -*-

import wx

boottomsize = (100, 30)
bottomborder = 20


class MyDialog(wx.Dialog):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.SetSize(800, 400)

        # class MyFrame1(wx.Frame):
        #     def __init__(self, parent, title):
        #         super().__init__(parent, title=title, size=(800, 400))

        # -----------иконка слева от названия программы----------------
        ico = wx.Icon('image/253.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(wx.Icon(ico))

        # -----------бокс  меню----------------
        panel = wx.Panel(self)

        font = wx.SystemSettings.GetFont(wx.SYS_DEFAULT_GUI_FONT)
        font.SetPointSize(12)
        panel.SetFont(font)

        box = wx.BoxSizer(wx.VERTICAL)  # вертикальное расположение боксов
        # ----------------------------------------------------------
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        # hbox = wx.BoxSizer()

        fb = wx.FlexGridSizer(7, 3, 10, 10)
        fb.AddMany([(wx.StaticText(panel, label="Путь к Excel файлу:")),
                    (wx.TextCtrl(panel), wx.ID_ANY, wx.EXPAND),
                    (wx.Button(panel, label='Открыть', size=boottomsize)),
                    (wx.StaticText(panel, label="Путь к Putty.exe:")),
                    (wx.TextCtrl(panel), wx.ID_ANY, wx.EXPAND),
                    (wx.Button(panel, label='Открыть', size=boottomsize)),
                    (wx.StaticText(panel, label="Путь к папке с фотографиями:")),
                    (wx.TextCtrl(panel), wx.ID_ANY, wx.EXPAND),
                    (wx.Button(panel, label='Открыть', size=boottomsize)),
                    (wx.StaticText(panel, label="Имя столбца таблицы:")),
                    (wx.TextCtrl(panel), wx.ID_ANY, wx.EXPAND),
                    (wx.Button(panel, label='Открыть', size=boottomsize)),
                    (wx.StaticText(panel, label="Путь к архиву с паролями:")),
                    (wx.TextCtrl(panel), wx.ID_ANY, wx.EXPAND),
                    (wx.Button(panel, label='Открыть', size=boottomsize)),
                    (wx.StaticText(panel, label="Пароль архива:")),
                    (wx.TextCtrl(panel), wx.ID_ANY, wx.EXPAND),
                    (wx.Button(panel, label='Открыть', size=boottomsize)),
                    (wx.StaticText(panel, label="О себе:")),
                    (wx.TextCtrl(panel, style=wx.NB_MULTILINE), wx.ID_ANY, wx.EXPAND)
                    ])
        # AddGrowableCol(self, col, proportion=0) proportion=1 для второго столбца (col=1)
        # AddGrowableRow(self, row, proportion=0) и для row=3 укажем proportion=1:
        fb.AddGrowableCol(1, 1)
        # fb.AddGrowableRow(3, 1)

        hbox.Add(fb, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        box.Add(hbox, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        # -----------------------------------------------------------------------------
        button7 = wx.Button(panel, label='Сохранить!!!', size=boottomsize)
        box.Add(button7, flag=wx.CENTER | wx.BOTTOM, border=10)

        panel.SetSizer(box)  # вертикальное расположение боксов отражение на экране
