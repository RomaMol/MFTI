#!/usr/bin/env python
# -*- coding: utf8 -*-

#  https://www.youtube.com/watch?v=VP6GqhNxy5E
#  wxPython #13: графика - контекст устройства, Pen, Brush и градиентная заливка

# wx.MemoryDC – контекст памяти (рисование в объекте Bitmap, расположенном в памяти устройства);
# wx.PrinterDC – контекст принтера (для ОС Windows и Mac);
# wx.ScreenDC – контекст экрана устройства (рисование на экране без привязки к окну);
# wx.ClientDC, wx.PaintDC – рисование в клиентской области окна;
# wx.WindowDC – рисование во всем окне.


import wx


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, pos=(0, 0), size=(700, 400))

        # wx.CallLater(100, self.onDraw)
        self.Bind(wx.EVT_PAINT, self.OnPaint)
        self.Bind(wx.EVT_PAINT, self.OnPaint1)
        self.Bind(wx.EVT_PAINT, self.OnPaint3)
        self.Bind(wx.EVT_PAINT, self.OnPaint4)
        self.Bind(wx.EVT_PAINT, self.OnPaint5)

    # def onDraw(self):
    #     dc = wx.ClientDC(self)
    #     dc.DrawLine(10, 40, 210, 140)

    def OnPaint(self, e):
        dc = wx.PaintDC(self)
        dc.DrawLine(50, 60, 190, 60)

        dc.SetPen(wx.Pen('#fdc073'))

        dc.DrawLine(0, 0, 200, 100)
        dc.DrawRectangle(300, 10, 200, 100)

        # Brush(colour, style=BRUSHSTYLE_SOLID)

    def OnPaint1(self, e):
        dc = wx.PaintDC(self)
        dc.SetPen(wx.Pen(wx.BLUE, 5, wx.LONG_DASH))

        dc.DrawLine(0, 0, 200, 100)

        dc.SetBrush(wx.Brush('#3F4137', wx.BDIAGONAL_HATCH))
        dc.DrawRectangle(300, 10, 200, 100)

        dc.SetBrush(wx.Brush(wx.YELLOW, wx.CROSSDIAG_HATCH))
        dc.DrawRectangle(10, 150, 100, 100)

        dc.SetBrush(wx.Brush(wx.GREEN, wx.CROSS_HATCH))
        dc.DrawRectangle(200, 150, 100, 100)

        dc.SetBrush(wx.Brush(wx.RED, wx.VERTICAL_HATCH))
        dc.DrawRectangle(400, 150, 100, 100)

    def OnPaint3(self, e):
        dc = wx.PaintDC(self)
        pen = wx.Pen(wx.BLUE, 10)

        pen.SetCap(wx.CAP_BUTT)
        dc.SetPen(pen)
        dc.DrawLine(30, 150, 150, 150)

        pen.SetCap(wx.CAP_PROJECTING)
        dc.SetPen(pen)
        dc.DrawLine(30, 190, 150, 190)

        pen.SetCap(wx.CAP_ROUND)
        dc.SetPen(pen)
        dc.DrawLine(30, 230, 150, 230)

        pen2 = wx.Pen('#4c4c4c', 1, wx.SOLID)
        dc.SetPen(pen2)
        dc.DrawLine(30, 130, 30, 250)
        dc.DrawLine(150, 130, 150, 250)
        dc.DrawLine(155, 130, 155, 250)

    def OnPaint4(self, e):
        dc = wx.PaintDC(self)
        rect = self.GetClientRect()
        pen = wx.Pen(wx.BLUE, 0, wx.TRANSPARENT)
        dc.SetPen(pen)

        dc.SetBrush(wx.Brush(wx.Bitmap('pattern1.png')))
        dc.DrawRectangle(0, 0, rect.width, rect.height)

    def OnPaint5(self, e):
        dc = wx.PaintDC(self)
        dc.GradientFillLinear((10, 10, 600, 50), '#00cc00', '#444444', wx.NORTH)
        dc.GradientFillLinear((10, 80, 600, 50), '#0000cc', '#444444', wx.SOUTH)
        dc.GradientFillLinear((10, 140, 600, 50), '#cc0000', '#444444', wx.EAST)
        dc.GradientFillLinear((10, 200, 600, 50), '#ffccff', '#444444', wx.WEST)


if __name__ == '__main__':
    app = wx.App()  # инициируем запуска приложения
    frame = MyFrame(None, title="Hello world", )  # главное окно программы
    frame.Center()  # разместить по центру
    frame.Show()  # показать на экране
    app.MainLoop()  # Главный цикл запуска приложения
