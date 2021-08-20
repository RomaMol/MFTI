#!/usr/bin/env python
# -*- coding: utf8 -*-

#  https://www.youtube.com/watch?v=90-JemgyMlU
#  wxPython #9: стандартные диалоговые окна
# wx.MessageBox(message, caption=MessageBoxCaptionStr, style=OK|CENTRE, parent=None, x=DefaultCoord, y=DefaultCoord)
#
# message – сообщение внутри окна;
# caption – заголовок окна;
# style – стилизация окна (в том числе элементами интерфейса);
# parent – ссылка на родительский элемент (обычно окно);
# x, y – координаты расположения диалогового окна.


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

        dlg = wx.MessageBox('Вы дейстительно хотите выйти из программы?', 'Вопрос',
                            wx.YES_NO | wx.NO_DEFAULT | wx.ICON_INFORMATION, self)
        if dlg == wx.YES:
            print("Нажата кнопка (да)")
        elif dlg == wx.NO:
            print("Нажата кнопка (нет)")

    def onQuit2(self, e):
        # MessageDialog(parent, message, caption=MessageBoxCaptionStr, style=OK|CENTRE, pos=DefaultPosition)

        dlg = wx.MessageDialog(self, 'Вы дейстительно хотите выйти из программы?', 'Вопрос',
                               wx.YES_NO | wx.NO_DEFAULT | wx.ICON_HAND)

        res = dlg.ShowModal()
        if res == wx.ID_YES:
            print("Нажата кнопка (да)")
        elif res == wx.ID_NO:
            print("Нажата кнопка (нет)")


if __name__ == '__main__':
    app = wx.App()  # инициируем запуска приложения
    frame = MyFrame(None, title="Hello world", )  # главное окно программы
    frame.Center()  # разместить по центру
    frame.Show()  # показать на экране
    app.MainLoop()  # Главный цикл запуска приложения
