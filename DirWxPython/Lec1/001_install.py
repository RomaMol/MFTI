#  https://www.youtube.com/watch?v=ntdYALwnF2g&list=PLA0M1Bcd0w8zyJOJXbvTKROHs2JJVGB6C&index=1
#  wxPython #1: обзор модулей для GUI и порядок установки wxPython"""

#  Установка модуля  wxPython
#  python.exe -m pip install --upgrade pip  обновление пакета
#
#  https://pypi.org/search/?q=WxPython
#  Занятие по установке пакетов: https://youtu.be/bVYvtpMeepU
#  во вкладке терминал набираем строку  pip install wxPython
#  pip freeze - роверка установленных  пакетов
#  проверка коректности работы программмы работы  WxPython
import wx

app = wx.App()  # инициируем запуска приложения
frame = wx.Frame(None, id=1, title="Hello world", )  # главное окно программы  None - самое главное не от кого не наследуется
frame.Center()  # разместить по центру
frame.Show()  # показать на экране


app.MainLoop()  # Главный цикл запуска приложения

# https://docs.wxpython.org
