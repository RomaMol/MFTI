#!/usr/bin/env python
# -*- coding: utf8 -*-

#  https://youtu.be/DdHMnHeX5rY
#  wxPython #7: механизм обработки событий - Bind, Unbind

# wx.EVT_BUTTON – событие, генерируемое виджетом wx.Button;
# wx.EVT_MENU – событие, генерируемое меню;
# wx.EVT_TEXT – событие, генерируемое wx.TextCtrl;
# wx.EVT_TOOL – событие, генерируемое toolbox;
# wx.EVT_MOVE – событие при перемещении окна;
# wx.EVT_PAINT – событие при перерисовки элемента (обычно, окна);
# wx.EVT_KEY_DOWN – событие при нажатии на клавишу;
# wx.EVT_KEY_UP – событие при отпускании клавиши.

import wx

ID_EXIT = 1

bottom3 = 3
bottom4 = 4


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title)

        # -------------------------Bind, Unbind ----------------------------------------------------
        panel = wx.Panel(self)
        btn1 = wx.Button(panel, wx.ID_ANY, "Кнопка 1")

        btn1.Bind(wx.EVT_BUTTON, self.onButton1, )
        panel.Bind(wx.EVT_BUTTON, self.onButtonpanel, )
        self.Bind(wx.EVT_BUTTON, self.onButtonframe, )
        panel.Unbind(wx.EVT_BUTTON)

        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

    def OnCloseWindow(self, event):
        dial = wx.MessageDialog(None, 'Вы действительно хотите выйти?', 'Вопрос',
                                wx.YES_NO | wx.NO_DEFAULT | wx.ICON_QUESTION)

        ret = dial.ShowModal()

        if ret == wx.ID_YES:
            self.Destroy()
        else:
            event.Veto()

    def onButton1(self, event):
        print("уровень кнопки")
        event.Skip()

    def onButtonpanel(self, event):
        print("уровень панели")
        event.Skip()

    def onButtonframe(self, event):
        print("уровень окна")
        event.Skip()


if __name__ == '__main__':
    app = wx.App()  # инициируем запуска приложения
    frame = MyFrame(None, title="Hello world", )  # главное окно программы
    frame.Center()  # разместить по центру
    frame.Show()  # показать на экране
    app.MainLoop()  # Главный цикл запуска приложения
