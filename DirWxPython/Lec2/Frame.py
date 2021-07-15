#  https://www.youtube.com/watch?v=9errl8RTA-M&list=PLA0M1Bcd0w8zyJOJXbvTKROHs2JJVGB6C&index=2
#  wxPython #2: общая структура интерфейса
import wx

"""
PopupWindow – специальный оконный класс для создания popup меню, списков combobox 
    и других вспомогательных виджетов подобного рода;
ScrolledWindow – используется для создания окна с прокручиваемым содержимым;
Frame – используется для создания стандартного окна;
MDIParentFrame (Multiple Document Interface) – класс, содержащий дочерние 
    оконные классы (как пример, Photoshop со множеством открытых документов);
MDIChildFrame – создает окно внутри класса MDIParentFrame;
Dialog – создает диалоговое окно.

"""


class MyFrame(wx.Frame):
    def __init__(self, parent,  title):
        super().__init__(parent,  title=title)


class MyFrame2(wx.MDIParentFrame ):
    def __init__(self, parent, title):
        super().__init__(parent, -1, title)
        menubar = wx.MenuBar()
        self.SetMenuBar(menubar)
        win = wx.MDIChildFrame(self, -1, "Child Window", size=(200, 150))
        win.Show()


app = wx.App()  # инициируем запуска приложения
frame = MyFrame2(None, title="Hello world", )  # главное окно программы


frame.Center()  # разместить по центру
frame.Show()  # показать на экране

app.MainLoop()  # Главный цикл запуска приложения
