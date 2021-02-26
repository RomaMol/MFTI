#   https://www.youtube.com/watch?v=4N-Q74IJd9U&list=PLA0M1Bcd0w8zo9ND-7yEFjoHBg_fzaQ-B&index=8
#   ООП Python 3 #8: множественное наследование, функция super

# ---


class Point:
    """
     координаты точки
     x = 1 y = 1  атрибуты == данные
     def fun()  - методы == функции
    """

    def __init__(self, x=0, y=0):
        """ методы обявления локальных переменных принимающих значения """
        print(" конструктора базового класса Point  def __init__")
        self.__x = x
        self.__y = y

    def __str__(self):
        """Метод __str__ стандартное значение Метода __str__   <__main__.Point object at 0x0000000001E66580>
        Метод __str__ переопределяем чтобы получать читаемые координаты
        """
        return f'({self.__x}, {self.__y})'


class Position:
    """Класс позиция координаты"""

    def __init__(self, sp: Point, ep: Point, *args):
        print(" конструктора  класса Position  def __init__")
        self._sp = sp
        self._ep = ep
        super().__init__(*args)


class Style:
    """Класс стили """

    def __init__(self, color: str = "red", wight: int = 1, *args):
        print(" конструктора  класса Style  def __init__ ")

        self._color = color
        self._wight = wight
        super().__init__(*args)


class Line(Position, Style):
    """'этот класс наследует координаты x=0, y=0 из класса Point
    def __init__ наследует у класса  Prop
    плохая практика вызыва класс Prop.__init__(self, *args) для переопределения
    возможны ошибки лучьше использовать метод супер  super()
    """

    def draw_line(self):
        print(f'Рисуем линию : {self._sp},{self._ep},{self._color},{self._wight}')


class Line1(Style, Position):
    """'этот класс наследует координаты x=0, y=0 из класса Point
    def __init__ наследует у класса  Prop
    плохая практика вызыва класс Prop.__init__(self, *args) для переопределения
    возможны ошибки лучьше использовать метод супер  super()
    """


    def draw_line(self):
        print(f'Рисуем линию : {self._sp},{self._ep},{self._color},{self._wight}')


l1 = Line(Point(0, 0), Point(300, 300))
print()
l1.draw_line()
l2 = Line1(Point(0, 0), Point(300, 300))# необходимо помнить последовательность классов
print()
l2.draw_line()
