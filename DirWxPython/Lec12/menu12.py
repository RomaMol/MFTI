#!/usr/bin/env python
# -*- coding: utf8 -*-

#  https://www.youtube.com/watch?v=F7XNGwDRQHg
#  wxPython #12: продвинутая работа с виджетами - ListBox, SplitterWindow, HtmlWindow, Notebook

# Документация по wxPython: https://docs.wxpython.org
#                           https://docs.wxpython.org/wx.lib.mixins.listctrl.ColumnSorterMixin.html
import wx
import wx.html
import wx.lib.mixins.listctrl

books = {1: ('Евгений Онегин', 'Пушкин А.С.', 2000, 192),
         2: ('Пиковая дама', 'Пушкин А.С.', 2004, 150.53),
         3: ('Мастер и Маргарита', 'Булгаков М.А.', 2005, 500),
         4: ('Роковые яйца', 'Булгаков М.А.', 2003, 400),
         5: ('Белая гвардия', 'Булгаков М.А.', 2010, 340)}


class ListCtrlMixins(wx.ListCtrl, wx.lib.mixins.listctrl.ListCtrlAutoWidthMixin,
                     wx.lib.mixins.listctrl.ColumnSorterMixin, wx.lib.mixins.listctrl.CheckListCtrlMixin):
    def __init__(self, parent, *args, **kw):
        wx.ListCtrl.__init__(self, parent, wx.ID_ANY, style=wx.LC_REPORT)
        wx.lib.mixins.listctrl.ListCtrlAutoWidthMixin.__init__(self)
        wx.lib.mixins.listctrl.ColumnSorterMixin.__init__(self, len(books))
        wx.lib.mixins.listctrl.CheckListCtrlMixin.__init__(self)

        self.itemDataMap = books

    def GetListCtrl(self):
        return self

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(800, 450))

        tabs = wx.Notebook(self, id=wx.ID_ANY)
        splitter = wx.SplitterWindow(tabs, wx.ID_ANY, style=wx.SP_LIVE_UPDATE)
        self.urls = ["htm/1_1.htm", "htm/1_2.htm", "htm/1_3.htm",
                     "htm/1_4.htm", "htm/1_5.htm"]
        listbox = wx.ListBox(splitter, choices=self.urls)

        self.htmlwin = wx.html.HtmlWindow(splitter, wx.ID_ANY, style=wx.NO_BORDER)
        self.htmlwin.SetStandardFonts(12)
        self.htmlwin.LoadPage(self.urls[0])

        splitter.SplitVertically(listbox, self.htmlwin)
        splitter.SetMinimumPaneSize(100)
        tabs.InsertPage(0, splitter, "Главная", select=True)

        #self.list = wx.ListCtrl(tabs, wx.ID_ANY, style=wx.LC_REPORT)
        self.list = ListCtrlMixins(tabs)
        self.list.SetFont(wx.Font(wx.FontInfo(12)))
        self.list.SetBackgroundColour("#f0f0f0")

        self.list.InsertColumn(0, 'Название', width=200)
        self.list.InsertColumn(1, 'Автор', width=200)
        self.list.InsertColumn(2, 'Год издания', wx.LIST_FORMAT_RIGHT, 140)
        self.list.InsertColumn(3, 'Цена', wx.LIST_FORMAT_RIGHT, 90)

        tabs.InsertPage(1, self.list, "Список книг")

        listbox.Bind(wx.EVT_LISTBOX, self.OnSelectUrl)

        for key, b in books.items():
            index = self.list.Append(b)
            self.list.SetItemData(index, key)

    def OnSelectUrl(self, e):
        urlId = e.GetEventObject().GetSelection()
        if urlId != wx.NOT_FOUND:
            self.htmlwin.LoadPage(self.urls[urlId])


if __name__ == '__main__':
    app = wx.App()  # инициируем запуска приложения
    frame = MyFrame(None, title="Hello world", )  # главное окно программы
    frame.Center()  # разместить по центру
    frame.Show()  # показать на экране
    app.MainLoop()  # Главный цикл запуска приложения
