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

from DirWxPython.Lec3.menu.mymenu2 import ViewMenu

ID_EXIT = 1
VIEW_STATUS = 2
VIEW_RGB = 3
VIEW_SRGB = 4


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title)


        menubar = wx.MenuBar()  # создание менюбара
        fileMenu = wx.Menu()  # создания вкладки меню; ITEM_NORMAL

        expMenu = wx.Menu()  # создания вкладки подменю; ITEM_NORMAL

        viewMenu = wx.Menu()  # создания вкладки меню;

        fileMenu.Append(wx.ID_NEW, '&Новый\tCtrl+N')
        fileMenu.Append(wx.ID_OPEN, '&Открыть\tCtrl+O')
        fileMenu.Append(wx.ID_SAVE, '&Сохранить\tCtrl+S')

        expMenu.Append(wx.ID_ANY, "Экспорт изображения")
        expMenu.Append(wx.ID_ANY, "Экспорт видео")
        expMenu.Append(wx.ID_ANY, "Экспорт данных")

        fileMenu.AppendSubMenu(expMenu, "&Экспорт")

        fileMenu.AppendSeparator()  # создания вкладки меню; ITEM_SEPARATOR

        item = wx.MenuItem(fileMenu, ID_EXIT, "Выход\tCtrl+Q", "Выход из приложения")
        item.SetBitmap(wx.Bitmap('png/exit16.png'))
        fileMenu.Append(item)
        # item = fileMenu.Append(
        #     wx.MenuItem(fileMenu, wx.ID_EXIT, "Выход\tCtrl+Q", "Выход из приложения"))  # создания отдельного пункта.

        self.vStatus = viewMenu.Append(VIEW_STATUS, 'Статустная строка', kind=wx.ITEM_CHECK)
        self.vRgb = viewMenu.Append(VIEW_RGB, 'Тип RGB', 'Тип RGB', kind=wx.ITEM_RADIO)
        self.vSrgb = viewMenu.Append(VIEW_SRGB, 'Тип sRGB', 'Тип sRGB', kind=wx.ITEM_RADIO)

        menubar.Append(fileMenu, "&File")  # отражение вкладки меню в окне
        menubar.Append(viewMenu, "&Вид")
        self.SetMenuBar(menubar)  # создание менюбара отражение панели в окне

        self.Bind(wx.EVT_MENU, self.onQuit, id=ID_EXIT)

        self.Bind(wx.EVT_MENU, self.onStatus, id=VIEW_STATUS)
        self.Bind(wx.EVT_MENU, self.onImageType, id=VIEW_RGB)
        self.Bind(wx.EVT_MENU, self.onImageType, id=VIEW_SRGB)

    def onQuit(self, event):
        self.Close()

    def onStatus(self, event):
        if self.vStatus.IsChecked():
            print("Показать статусную строку")
        else:
            print("Скрыть статусную строку")

    def onImageType(self, event):
        if self.vRgb.IsChecked():
            print("Режим RGB")
        elif self.vSrgb.IsChecked():
            print("Режим sRGB")