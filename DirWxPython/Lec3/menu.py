#  https://www.youtube.com/watch?v=Y__0Xrm0Mp0&list=PLA0M1Bcd0w8zyJOJXbvTKROHs2JJVGB6C&index=3
#  wxPython #3: создание меню и подменю - MenuBar, Menu, MenuItem, Bind, Append, AppendSeparator
import wx

from DirWxPython.Lec3.menu.mymenu import MyFrame

app = wx.App()  # инициируем запуска приложения
frame = MyFrame(None, title="Hello world", )  # главное окно программы

frame.Center()  # разместить по центру
frame.Show()  # показать на экране

app.MainLoop()  # Главный цикл запуска приложения
