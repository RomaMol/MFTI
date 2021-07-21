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
        vbox = wx.BoxSizer(wx.VERTICAL)

        btn1 = wx.Button(panel, wx.ID_ANY, "Кнопка 1")
        btn2 = wx.Button(panel, wx.ID_ANY, "Кнопка 2")
        btn3 = wx.Button(panel, bottom3, "Кнопка 3")
        btn4 = wx.Button(panel, bottom4, "Кнопка 4")
        btn1.SetPosition(wx.Point(10, 10))
        btn2.SetPosition(wx.Point(200, 10))
        btn3.SetPosition(wx.Point(10, 50))
        btn4.SetPosition(wx.Point(200, 50))

        panel.SetSizer(vbox)
        panel.Bind(wx.EVT_LEFT_DOWN, self.OnLeftDown)

        self.Bind(wx.EVT_BUTTON, self.onButton1, id=btn1.GetId())
        self.Bind(wx.EVT_BUTTON, self.onButton2, id=btn2.GetId())
        self.Bind(wx.EVT_BUTTON, self.onButton3, btn3)
        self.Bind(wx.EVT_BUTTON, self.onButton4, btn4)

    def OnLeftDown(self, event):
        print("Нажатие на левую кнопку мыши")

    def onButton1(self, event):
        print("Нажатие на 1 кнопку мыши")

    def onButton2(self, event):
        print("Нажатие на 2 кнопку мыши")

    def onButton3(self, event):
        print("Нажатие на 3 кнопку мыши")

    def onButton4(self, event):
        print("Нажатие на 4 кнопку мыши")

    def onQuit(self, event):
        self.Close()


if __name__ == '__main__':
    app = wx.App()  # инициируем запуска приложения
    frame = MyFrame(None, title="Hello world", )  # главное окно программы
    frame.Center()  # разместить по центру
    frame.Show()  # показать на экране
    app.MainLoop()  # Главный цикл запуска приложения
