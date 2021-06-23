#!/usr/bin/python
# -*- coding: utf-8 -*-

#   https://youtu.be/ZzWdGLuq69E
#   Python 3 #25: форматирование строк: метод format и F-строки
#

pol = {"M": "Уважаемый", "W": "Уважаемая"}
user = {("Иван Федорович", 18, "M"),
        ("Николай Иванович", 28, "M"),
        ("Анна Антоновна", 15, "W"),
        ("Ольга Ивановна", 17, "W") }

for person in user:
    msg = f"""{pol[person[2]]} {person[0]}!
Поздравем вас с {person[1]} летием !!! """
    print(msg, end="\n\n")
