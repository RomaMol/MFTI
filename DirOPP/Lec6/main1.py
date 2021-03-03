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
        self.__wight = wight  # 1 - частное свойство атрибуты данные

    def get_witch(self):
        """ передача частного свойство (атрибуты данные)  __wight """
        return self.__wight


class Line(Prop):
    """'этот класс наследует координаты x=0, y=0 из класса Point
    def __init__ наследует у класса  Prop
    плохая практика вызыва класс Prop.__init__(self, *args) для переопределения
    возможны ошибки --- лучьше использовать  методы функции супер()   super().__init__(*args) без self !!!
    super() --  ранжирует классы выставляя по порядку наследования
    """

    def __init__(self, *args):
        print("переопределение конструктора базового класса Line")
        super().__init__(*args)

    def draw_line(self):
        # 'Line' object has no attribute '_Line__wight'   --> def get_witch(self):
        # так как частная переменная создана в  class Prop:
        # {self.__wight} --> {self.get_witch()}
        print(f'Рисуем линию : {self._sp},{self._ep},{self._color},{self.get_witch()}')


class Rect(Prop):
    def __init__(self, *args):
        print("переопределение конструктора базового класса Rect")
        super().__init__(*args)
        self.__wight = 5 # переопределение свойства


    def draw_rect(self):
        """ после переопределения свойства self.__wight = 5
        {self.__wight} -- будет 5
        {self.get_witch() -- будет 1
        """
        print(f'Рисуем Rect get_witch : {self._sp},{self._ep},{self._color},{self.get_witch()}')
        print(f'Рисуем Rect __wight   : {self._sp},{self._ep},{self._color},{self.__wight}')


#  провека дейсвительно ли у класс Point базовый класс object
print("провека дейсвительно ли у класс Point базовый класс object:  ", issubclass(Point, object))

l1 = Line(Point(0, 0), Point(300, 300))
print(l1.__dict__)
# {'_sp': <__main__.Point object at 0x0000000002686130>, '_ep': <__main__.Point object at 0x00000000026861F0>,
# '_color': 'red', '_Prop__wight': 1}

l1.draw_line()
print()
r1 = Rect(Point(0, 0), Point(300, 300))
print(r1.__dict__)
r1.draw_rect()
