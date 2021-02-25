#   https://www.youtube.com/watch?v=VQ6vUzqAInU&list=PLA0M1Bcd0w8zo9ND-7yEFjoHBg_fzaQ-B&index=6
#   ООП Python 3 #6: простое наследование классов, режим доступа protected

# ---


class Point:
    """
     класс не явно наследуется от класса  ---  object

     x = 1 y = 1  атрибуты == данные
     def fun()  - методы == функции
    """

    def __init__(self, x=0, y=0):
        """ методы обявления локальных переменных принимающих значения """
        print(" конструктора базового класса Point")
        self.__x = x
        self.__y = y

    def __str__(self):
        """Метод __str__
        стандартное значение Метода __str__   <__main__.Point object at 0x0000000001E66580>
        Метод __str__ переопределяем
        чтобы получать читаемые координаты
        """
        return f'({self.__x}, {self.__y})'


class Prop:
    """
    _ep - одно _ предостерегает использование свойства вне класс Prop
    """
    def __init__(self, sp: Point, ep: Point, color: str = "red", wight: int = 1):
        print(" конструктора базового класса Prop")
        self._sp = sp
        self._ep = ep
        self._color = color
        self._wight = wight

    @property
    def ep(self):
        return self._ep


class Line(Prop):
    """'этот класс наследует координаты x=0, y=0 из класса Point
    def __init__ наследует у класса  Prop
    плохая практика вызыва класс Prop.__init__(self, *args) для переопределения
    возможны ошибки лучьше использовать метод супер  super()
    """
    def __init__(self, *args):
        print("переопределение конструктора базового класса Line")
        Prop.__init__(self, *args)


    def draw_line(self):
        print(f'Рисуем линию : {self._sp},{self._ep},{self._color},{self._wight}')


class Rect(Prop):
    def draw_rect(self):
        print(f'Рисуем Rect : {self._sp},{self._ep},{self._color},{self._wight}')


#  провека дейсвительно ли у класс House базовый класс object
print("провека дейсвительно ли у класс House базовый класс object:  ", issubclass(Point, object))

l1 = Line(Point(0, 0), Point(300, 300))
print()
l1.draw_line()
print()
r1 = Rect(Point(0, 0), Point(300, 300))
r1.draw_rect()
