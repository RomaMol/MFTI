#  https://www.youtube.com/watch?v=6NCmQwVPXFU&list=PLA0M1Bcd0w8zyJOJXbvTKROHs2JJVGB6C&index=4
#  wxPython #4: контекстное меню и панель инструментов (toolbar)

import wx

from DirWxPython.Lec4.menu.mymenu import MyFrame

app = wx.App()  # инициируем запуска приложения
frame = MyFrame(None, title="Hello world", )  # главное окно программы

frame.Center()  # разместить по центру
frame.Show()  # показать на экране

app.MainLoop()  # Главный цикл запуска приложения
