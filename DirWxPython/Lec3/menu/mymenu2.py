#!/usr/bin/env python
# -*- coding: utf8 -*-

#  https://www.youtube.com/watch?v=Y__0Xrm0Mp0&list=PLA0M1Bcd0w8zyJOJXbvTKROHs2JJVGB6C&index=3
#  wxPython #3: создание меню и подменю - MenuBar, Menu, MenuItem, Bind, Append, AppendSeparator

# MenuBar – для создания панели меню;
# Menu – для создания вкладки меню;
# MenuItem – для создания отдельного пункта.

# ITEM_NORMAL – обычный текст;
# ITEM_SEPARATOR – разделитель (сепаратор);
# ITEM_CHECK – пункт с флажком;
# ITEM_RADIO – пункт с возможностью перебора.

#               Bind(event, handler, source=None)
#           event – тип события, связанный с определенным интерфейсным объектом;
#           handler – ссылка на функцию-обработчик;
#           source – источник, генерирующий событие.
import wx

ID_EXIT = 1


class ViewMenu(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title)

        viewMenu = wx.Menu()  # создания вкладки меню;

        viewMenu.Append(wx.ID_ANY, 'Статустная строка', kind=wx.ITEM_CHECK)
        viewMenu.Append(wx.ID_ANY, 'Тип RGB', 'Тип RGB', kind=wx.ITEM_RADIO)
        viewMenu.Append(wx.ID_ANY, 'Тип sRGB', 'Тип sRGB', kind=wx.ITEM_RADIO)

        self.Bind(wx.EVT_MENU, self.onQuit, id=ID_EXIT)

    def onQuit(self, event):
        self.Close()
