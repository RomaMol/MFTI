#!/usr/bin/env python
# -*- coding: utf8 -*-

#  https://youtu.be/dSBY6F8qsmM
#  wxPython #8: примеры событий, назначение id виджетам

# wx.EVT_MOTION
import wx

ID_EXIT = 1


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title)

        # -------------------------wx.EVT_MOTION ----------------------------------------------------
        # ----------- в котором будем отображать текущие координаты

        self.x = wx.StaticText(self, label='x:', pos=(10, 10))
        self.y = wx.StaticText(self, label='y:', pos=(10, 30))

        self.Bind(wx.EVT_MOTION, self.OnMove)

        # -------------------------wx.EVT_PAINT----------------------------------------------------
        # ---   событие возникает при перерисовки окна или его отдельного элемента

        self.Bind(wx.EVT_PAINT, self.OnPaint)

        # -------------------------wx.EVT_SET_FOCUS, wx.EVT_KILL_FOCUS----------------------------------------------------
        # - два события срабатывают в момент получения элементом фокуса и в момент его потери.

        t1 = wx.TextCtrl(self)
        t2 = wx.TextCtrl(self)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(t1, flag=wx.EXPAND | wx.ALL, border=10)
        vbox.Add(t2, flag=wx.EXPAND | wx.ALL, border=10)
        self.SetSizer(vbox)
        t1.Bind(wx.EVT_SET_FOCUS, self.OnSetFocus)
        t1.Bind(wx.EVT_KILL_FOCUS, self.OnKillFocus)

        t2.Bind(wx.EVT_SET_FOCUS, self.OnSetFocus)
        t2.Bind(wx.EVT_KILL_FOCUS, self.OnKillFocus)

    def OnSetFocus(self, event):
        event.GetEventObject().SetBackgroundColour("#FFFFE5")
        event.Skip()

    def OnKillFocus(self, event):
        event.GetEventObject().SetBackgroundColour("#fff")
        event.Skip()

    def OnPaint(self, event):
        print("событие EVT_PAINT")
        dc = wx.PaintDC(self)
        dc.DrawLine(0, 0, 100, 100)

    def OnMove(self, event):
        x, y = event.GetPosition()
        self.x.SetLabel('x: ' + str(x))
        self.y.SetLabel('y: ' + str(y))






if __name__ == '__main__':
    app = wx.App()  # инициируем запуска приложения
    frame = MyFrame(None, title="Hello world", )  # главное окно программы
    frame.Center()  # разместить по центру
    frame.Show()  # показать на экране
    app.MainLoop()  # Главный цикл запуска приложения
