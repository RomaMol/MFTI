#!/usr/bin/env python
# -*- coding: utf8 -*-

#  https://www.youtube.com/watch?v=YLJmdxjI5GU
#  wxPython #10: пользовательские диалоговые окна, класс Dialog
# wx.Dialog(parent, id=ID_ANY, title="", pos=DefaultPosition, size=DefaultSize,
# style=DEFAULT_DIALOG_STYLE, name=DialogNameStr)

# parent – ссылка на родительское окно (или значение None);
# id – идентификатор окна;
# title – заголовок окна;
# pos, size – позиция и размер окна;
# style – стилизация окна.


import wx


class MyDialog(wx.Dialog):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

        # self.Bind(wx.EVT_CLOSE, self.onClose)

    def Destroy(self):
        print("Вызван метод Destroy")
        super().Destroy()

    # -----------------------2-----------------------------
    # def onClose(self, e):
    #     self.Destroy()
    #     self.parent.dlg = None


class MyDlg(wx.Dialog):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.SetSize(500, 150)

        vb = wx.BoxSizer(wx.VERTICAL)
        vb.Add(wx.TextCtrl(self, wx.ID_ANY), flag=wx.EXPAND | wx.ALL, border=10)

        vh = wx.BoxSizer(wx.HORIZONTAL)
        bOk = wx.Button(self, wx.ID_OK, label="Да", size=(100, 30))
        bCn = wx.Button(self, wx.ID_CANCEL, label="Отмена", size=(100, 30))
        vh.Add(bOk, flag=wx.LEFT, border=10)
        vh.Add(bCn, flag=wx.LEFT, border=10)

        vb.Add(vh, flag=wx.ALIGN_CENTER | wx.ALL, border=10)
        self.SetSizer(vb)

        bOk.Bind(wx.EVT_BUTTON, self.onOk)
        bCn.Bind(wx.EVT_BUTTON, self.offbCn)

    def onOk(self, event):
        self.EndModal(wx.ID_OK)
        print(f"{wx.ID_OK}")

    def offbCn(self,e):
        self.EndModal(wx.ID_CANCEL)
        print(f"{wx.ID_CANCEL}")


class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(600, 300))

        toolbar = self.CreateToolBar()
        br_quit = toolbar.AddTool(wx.ID_ANY, "Выход", wx.Bitmap("exit32.png"))
        toolbar.AddSeparator()
        dialog = toolbar.AddTool(wx.ID_ANY, "Диалог", wx.Bitmap("exit32.png"))
        toolbar.AddSeparator()
        dlg = toolbar.AddTool(wx.ID_ANY, "Диалог", wx.Bitmap("exit32.png"))
        toolbar.Realize()

        self.Bind(wx.EVT_TOOL, self.onQuit, br_quit)
        self.Bind(wx.EVT_TOOL, self.onDialog, dialog)
        self.Bind(wx.EVT_TOOL, self.onDlg, dlg)

        self.dlg = None

    def onDlg(self, e):
        dlg = MyDlg(self, title="Мой диалог...")
        res = dlg.ShowModal()
        dlg.Destroy()
        print(f"onDlg res, {res}")

    def onDialog(self, e):
        # ----------------------------3----------------------------
        with MyDialog(self, title="Мой диалог...") as dlg:
            res = dlg.ShowModal()
            print(f"onDialog, {res}")

    # -----------------------1------------------------
    # if self.dlg is None:
    #     self.dlg = MyDialog(self, title="Мой диалог...")
    #     self.dlg.Show()

    # -----------------------2-----------------------------
    # try:
    #     dlg = MyDialog(self, title="Мой диалог...")
    #     res = dlg.ShowModal()
    #     print(res)
    # except Exception as e:
    #     print(e)
    # finally:
    #     dlg.Destroy()

    def onQuit(self, e):
        self.Close()


if __name__ == '__main__':
    app = wx.App()  # инициируем запуска приложения
    frame = MyFrame(None, title="Hello world", )  # главное окно программы
    frame.Center()  # разместить по центру
    frame.Show()  # показать на экране
    app.MainLoop()  # Главный цикл запуска приложения
