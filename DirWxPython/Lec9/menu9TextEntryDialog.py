#!/usr/bin/env python
# -*- coding: utf8 -*-

#  https://youtu.be/dSBY6F8qsmM
#  wxPython #8: примеры событий, назначение id виджетам
# TextEntryDialog(parent, message, caption=GetTextFromUserPromptStr, value="", style=TextEntryDialogStyle, pos=DefaultPosition)
#
# parent – ссылка на родительское окно (если нет, то None);
# message – сообщение перед строкой ввода;
# caption – заголовок окна;
# value – начальное значение в поле ввода;
# style – стиль окна;
# pos – позиция окна.


import wx


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title)

        toolbar = self.CreateToolBar()
        br_quit = toolbar.AddTool(wx.ID_ANY, "Выход", wx.Bitmap("exit32.png"))
        br_quit2 = toolbar.AddTool(wx.ID_ANY, "Выход", wx.Bitmap("exit32.png"))
        toolbar.Realize()

        self.Bind(wx.EVT_TOOL, self.onQuit, br_quit)
        self.Bind(wx.EVT_TOOL, self.onQuit2, br_quit2)


    def onQuit(self, e):

        dlg = wx.TextEntryDialog(self, "Введите имя", "Ввод данных...", "noname")
        res = dlg.ShowModal()
        if res == wx.ID_OK:
            print(dlg.GetValue())

    def onQuit2(self, e):

        dlg = wx.DirDialog(self, "Выбор директории...", "D:",
                           wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST)

        res = dlg.ShowModal()
        if res == wx.ID_OK:
            print("Выбран каталог: " + dlg.GetPath())


if __name__ == '__main__':
    app = wx.App()  # инициируем запуска приложения
    frame = MyFrame(None, title="Hello world", )  # главное окно программы
    frame.Center()  # разместить по центру
    frame.Show()  # показать на экране
    app.MainLoop()  # Главный цикл запуска приложения
