#  https://youtu.be/4tkvthAC3k8
#  wxPython #5: схемы (layout) размещения виджетов, BoxSizer

import wx

from DirWxPython.Lec5.menu.mymenuboxsizer import MyFrame

app = wx.App()  # инициируем запуска приложения
frame = MyFrame(None, title="Hello world", )  # главное окно программы

frame.Center()  # разместить по центру
frame.Show()  # показать на экране

app.MainLoop()  # Главный цикл запуска приложения
