# https://www.youtube.com/watch?v=zwel95I7O88&list=PLA0M1Bcd0w8zo9ND-7yEFjoHBg_fzaQ-B&index=4
# ООП Python 3 #4: объекты свойства (property) и дескрипторы классов

# ---  Дискрипторы ---

class PointValue:
    def __set_name__(self, owner, name):
        print(name)
        self.__name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.__name]

    def __set__(self, instance, value):
        instance.__dict__[self.__name] = value


class House:
    """Класс существительное с большой буквы
    x = 1 y = 1  атрибуты == данные
    def fun()  - методы == функции
    """
    pointX = PointValue()
    pointY = PointValue()

    def __init__(self, x=0, y=0, ):
        """открытые и закрытые атрибуты
        self.x   - открытые PUBLIC
        self.__x - закрытые PRIVATE
        """
        self.pointX = x
        self.pointY = y


h1 = House(1,2)
h2 = House(11,22)
h1.CorX = 12  # запись значения
x = h1.CorX  # чтение значения
print(h1.pointX,h1.pointY )
print(h2.pointX,h2.pointY )

