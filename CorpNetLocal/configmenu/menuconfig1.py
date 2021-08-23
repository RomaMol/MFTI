#!/usr/bin/env python
# -*- coding: utf8 -*-

import wx

bottom_size = (100, 30)  # Размер кнопки
bottom_border = 20

size_config = (800, 350)  # размер листа конфигурации ширинаХвысота

name_button = 'Открыть'
name_string = ["Путь к Excel файлу:", "Путь к Putty.exe:", "Путь к папке с фотографиями:", "Путь к архиву с паролями:",
               "Имя столбца таблицы:", "Пароль архива:"]


class MyDialog(wx.Dialog):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.SetSize(size_config)

        # -----------иконка слева от названия программы----------------
        ico = wx.Icon('image/253.ico', wx.BITMAP_TYPE_ICO)
        self.SetIcon(wx.Icon(ico))

        # -----------бокс  меню----------------
        panel = wx.Panel(self)

        font = wx.SystemSettings.GetFont(wx.SYS_DEFAULT_GUI_FONT)
        font.SetPointSize(10)
        panel.SetFont(font)

        box = wx.BoxSizer(wx.VERTICAL)  # вертикальное расположение боксов
        # ----------------------------------------------------------
        h_box = wx.BoxSizer(wx.HORIZONTAL)

        fb = wx.FlexGridSizer(7, 3, 10, 10)
        fb.AddMany([(wx.StaticText(panel, label=name_string[0])),
                    (wx.TextCtrl(panel), wx.ID_ANY, wx.EXPAND),
                    (wx.Button(panel, label=name_button, size=bottom_size)),
                    (wx.StaticText(panel, label=name_string[1])),
                    (wx.TextCtrl(panel), wx.ID_ANY, wx.EXPAND),
                    (wx.Button(panel, label=name_button, size=bottom_size)),
                    (wx.StaticText(panel, label=name_string[2])),
                    (wx.TextCtrl(panel), wx.ID_ANY, wx.EXPAND),
                    (wx.Button(panel, label=name_button, size=bottom_size)),
                    (wx.StaticText(panel, label=name_string[3])),
                    (wx.TextCtrl(panel), wx.ID_ANY, wx.EXPAND),
                    (wx.Button(panel, label=name_button, size=bottom_size)),
                    (wx.StaticText(panel, label=name_string[4])),
                    (wx.TextCtrl(panel), wx.ID_ANY, wx.EXPAND),
                    (wx.Button(panel, label=name_button, size=bottom_size)),
                    (wx.StaticText(panel, label=name_string[5])),
                    (wx.TextCtrl(panel), wx.ID_ANY, wx.EXPAND),
                    (wx.Button(panel, label=name_button, size=bottom_size)),
                    ])

        fb.AddGrowableCol(1, 1)

        h_box.Add(fb, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        box.Add(h_box, proportion=1, flag=wx.EXPAND | wx.ALL, border=10)
        # -----------------------------------------------------------------------------
        button7 = wx.Button(panel, label='Сохранить!!!', size=bottom_size)
        box.Add(button7, flag=wx.CENTER | wx.BOTTOM, border=10)

        panel.SetSizer(box)  # вертикальное расположение боксов отражение на экране
