# https://www.youtube.com/watch?v=WP2sqI2BkeY&list=PLA0M1Bcd0w8zo9ND-7yEFjoHBg_fzaQ-B&index=3
# ООП Python 3 #3: режимы доступа - public, private, protected. Геттеры и сеттеры

class House:
    """Класс существительное с большой буквы
    x = 1 y = 1  атрибуты == данные
    def fun()  - методы == функции
    """

    def __init__(self, x=0, y=0):
        """открытые и закрытые атрибуты
        self.x   - открытые PUBLIC
        self.__x - закрытые PRIVATE
        """

        self.__x = x
        self.__y = y

    def __checkValue(x):
        """Метод внутренней проверки  ненужен self
        доступ к внутреннему методу класса House.__checkValue(x)
        """
        if isinstance(x, int) or isinstance(x, float):
            return True
        return False

    def setCor(self, x, y):
        """доступ к закрытым атрибутам устанавливаем значение
        проверяем причастность к типу
        if House.__checkValue(x) and House.__checkValue(y):
        """
        if House.__checkValue(x) and House.__checkValue(y):
            self.__x = x
            self.__y = y
        else:
            print("Введите число")

    def getCor(self):
        """Возвращение картежа закрытых атрибутов"""
        return self.__x, self.__y


h1 = House(10, 20)
print("h1.getCor() -->", h1.getCor())

h2 = House()
h2.setCor(4, 22)
print("h2.getCor() -->", h2.getCor())

# --- допустимо но нестоит злоупортеблять -------
print("h2._House__x -->", h2._House__x)  # Обращение к закрытому атрибуту
print("House._House__checkValue(33) -->", House._House__checkValue(33))  # Обращение к закрытому методу
# ------------------------------------------------
