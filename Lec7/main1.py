#   https://www.youtube.com/watch?v=LVv8V94eZ9Y&list=PLA0M1Bcd0w8zo9ND-7yEFjoHBg_fzaQ-B&index=7
#   ООП Python 3 #7: переопределение и перегрузка методов, абстрактные методы

# ---


class Point:
    """
     координаты точки
     x = 1 y = 1  атрибуты == данные
     def fun()  - методы == функции
    """

    def __init__(self, x=0, y=0):
        """ методы обявления локальных переменных принимающих значения """
        print(" конструктора базового класса Point")
        self.__x = x
        self.__y = y

    def __str__(self):
        """Метод __str__ стандартное значение Метода __str__   <__main__.Point object at 0x0000000001E66580>
        Метод __str__ переопределяем чтобы получать читаемые координаты
        """
        return f'({self.__x}, {self.__y})'

    def is_digit(self):
        """Метод проверки введенных данных на int  float """
        if (isinstance(self.__x, int) or (isinstance(self.__x, float)) and
                (isinstance(self.__y, int) or (isinstance(self.__y, float)))):
            return True
        return False

    def is_int(self):
        """Метод проверки введенных данных на int  """
        if isinstance(self.__x, int) and isinstance(self.__y, int):
            return True
        return False


class Prop:
    """
    класс Prop общие свойства для рисования примитивов Line Rect
    """

    def __init__(self, sp: Point, ep: Point, color: str = "red", wight: int = 1):
        print(" конструктора базового класса Prop")
        self._sp = sp
        self._ep = ep
        self._color = color
        self._wight = wight

    def set_cords(self, sp, ep):
        """Метод проверки введенных данных на int  float """
        if sp.is_digit() and ep.is_digit():
            self._sp = sp
            self._ep = ep
        else:
            print(" координаты должны быть числа")


class Line(Prop):
    """'этот класс наследует координаты x=0, y=0 из класса Point
    def __init__ наследует у класса  Prop
    плохая практика вызыва класс Prop.__init__(self, *args) для переопределения
    возможны ошибки лучьше использовать метод супер  super()
    """

    def __init__(self, *args):
        print("переопределение конструктора базового класса Line")
        super().__init__(*args)  # Prop.__init__(self, *args)  только лучьше

    def draw_line(self):
        print(f'Рисуем линию : {self._sp},{self._ep},{self._color},{self._wight}')

    #     Перегрузка метода для работы как с одной так и двумя координатами
    def set_cords(self, sp: Point, ep: Point = None):
        """Переопределенный Метод для класса Линия проверки введенных данных на int  """
        if ep is None:
            if sp.is_int():
                self._sp = sp
            else:
                print(" координаты должны быть целые числа")
        else:
            if sp.is_int() and ep.is_int():
                Prop.set_cords(self, sp, ep)
            else:
                print(" координаты должны быть целые числа")


l1 = Line(Point(0, 0), Point(300, 300))
print()
l1.draw_line()
l1.set_cords(Point(200, 200), Point(30, 30))
l1.draw_line()
l1.set_cords(Point(40, 400))
l1.draw_line()
