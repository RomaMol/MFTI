#!/usr/bin/python
# -*- coding: utf-8 -*-

#    https://www.youtube.com/watch?v=nShaQEm3sRg&list=PLA0M1Bcd0w8zo9ND-7yEFjoHBg_fzaQ-B&index=21
#    21. ООП Python 3: инструкция raise и пользовательские исключения


print("Куда ты скачешь, гордый конь,")
print("И где опустишь ты копыта?")

# raise ArithmeticError("-----Делить на ноль нельзя!----")

print("Не так ли ты над самой бездной")
print("На высоте, уздой железной")
print("Россию поднял на дыбы?")


class printsentdata(Exception):
    """Пользовательский класс исключений"""

    def __init__(self, *args):
        super().__init__(*args)
        self.msg = args[0] if args else None
        # if args:
        #     self.msg = args[0]
        # else:
        #     self.msg = None

    def __str__(self):
        return print(f" oshibka:   {self.msg}")


class printdata:
    def print(self, data):
        self.send_data(data)
        print(f"print {str(data)}")

    def send_data(self, data):
        if not self.send_to_print(data):
            raise printsentdata("printer ne otvechaet")

    def send_to_print(self, data):
        return False


p = printdata()

p.print("123")

# try:
#     p.print("123")
# except printsentdata:
#     print("printer not dostup")
