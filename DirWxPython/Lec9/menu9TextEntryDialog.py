#!/usr/bin/env python
# -*- coding: utf8 -*-

#  https://www.youtube.com/watch?v=90-JemgyMlU
#  wxPython #9: стандартные диалоговые окна
# TextEntryDialog(parent, message, caption=GetTextFromUserPromptStr, value="", style=TextEntryDialogStyle, pos=DefaultPosition)
#
# parent – ссылка на родительское окно (если нет, то None);
# message – сообщение перед строкой ввода;
# caption – заголовок окна;
# value – начальное значение в поле ввода;
# style – стиль окна;
# pos – позиция окна.


import wx


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title)

        toolbar = self.CreateToolBar()
        data_input = toolbar.AddTool(wx.ID_ANY, "Ввод данных", wx.Bitmap("exit32.png"))
        select_dir = toolbar.AddTool(wx.ID_ANY, "Выбор директории", wx.Bitmap("exit32.png"))
        select_file = toolbar.AddTool(wx.ID_ANY, "Выбор файла", wx.Bitmap("exit32.png"))
        select_font = toolbar.AddTool(wx.ID_ANY, "Выбор шрифта", wx.Bitmap("exit32.png"))
        toolbar.Realize()

        self.Bind(wx.EVT_TOOL, self.Data_input, data_input)
        self.Bind(wx.EVT_TOOL, self.Select_dir, select_dir)
        self.Bind(wx.EVT_TOOL, self.Select_file, select_file)
        self.Bind(wx.EVT_TOOL, self.Select_font, select_font)


    def Data_input(self, e):

        dlg = wx.TextEntryDialog(self, "Введите имя", "Ввод данных...", "noname")
        res = dlg.ShowModal()
        if res == wx.ID_OK:
            print(dlg.GetValue())

    def Select_dir(self, e):

        dlg = wx.DirDialog(self, "Выбор директории...", "D:",
                           wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST)

        res = dlg.ShowModal()
        if res == wx.ID_OK:
            print("Выбран каталог: " + dlg.GetPath())

    def Select_file(self, e):

        with wx.FileDialog(self, "Открыть файл...", wildcard="Файлы Питона (*.py)|*.py",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return

            pathname = fileDialog.GetPath()
            print(pathname)

    def Select_font(self, e):

        dlg = wx.FontDialog(self)
        res = dlg.ShowModal()
        if res == wx.ID_OK:
            font = dlg.GetFontData().GetChosenFont()  # wx.Font
            print(font.GetFaceName())


if __name__ == '__main__':
    app = wx.App()  # инициируем запуска приложения
    frame = MyFrame(None, title="Hello world", )  # главное окно программы
    frame.Center()  # разместить по центру
    frame.Show()  # показать на экране
    app.MainLoop()  # Главный цикл запуска приложения
