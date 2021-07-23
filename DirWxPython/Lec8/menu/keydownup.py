#!/usr/bin/env python
# -*- coding: utf8 -*-

#  https://youtu.be/dSBY6F8qsmM
#  wxPython #8: примеры событий, назначение id виджетам

# wx.EVT_MOTION
import wx

ID_EXIT = 1

B3 = wx.NewIdRef()
B4 = wx.NewIdRef()
class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title)

        # -------------------------wx.EVT_KEY_DOWN, wx.EVT_KEY_UP ----------------------------------------------------
        # в котором будем отображать текущие координатыДанные события срабатывают при нажатии и отпускании клавиши на клавиатуре

        self.Bind(wx.EVT_KEY_DOWN, self.OnKeyDown)
        self.Bind(wx.EVT_KEY_UP, self.OnKeyUp)

        # ----------------      wx.ID_ANY  = -1 --------------------
        # print(b1.GetId(), b2.GetId(), sep="\n")
        b1 = wx.Button(self, -1, label="Кнопка 1")
        b2 = wx.Button(self, wx.ID_ANY, label="Кнопка 2")

        b3 = wx.Button(self, B3.GetId(), label="Кнопка 3")
        b4 = wx.Button(self, B4.GetId(), label="Кнопка 4")

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(b1, flag=wx.EXPAND | wx.ALL, border=10)
        vbox.Add(b2, flag=wx.EXPAND | wx.ALL, border=10)
        vbox.Add(b3, flag=wx.EXPAND | wx.ALL, border=10)
        vbox.Add(b4, flag=wx.EXPAND | wx.ALL, border=10)

        self.SetSizer(vbox)

        print(b1.GetId(), b2.GetId(), sep="\n")
        print(b3.GetId(), b4.GetId(), sep="\n")


    def OnKeyUp(self, e):
        print("Отпустили кнопку")

    def OnKeyDown(self, e):
        print("Нажали кнопку")
        key = e.GetKeyCode()
        if key == wx.WXK_ESCAPE:
            ret = wx.MessageBox('Вы дейстительно хотите выйти из программы?', 'Вопрос',
                                wx.YES_NO | wx.NO_DEFAULT, self)

            if ret == wx.YES:
                self.Close()




if __name__ == '__main__':
    app = wx.App()  # инициируем запуска приложения
    frame = MyFrame(None, title="Hello world", )  # главное окно программы
    frame.Center()  # разместить по центру
    frame.Show()  # показать на экране
    app.MainLoop()  # Главный цикл запуска приложения
