# https://www.youtube.com/watch?v=WP2sqI2BkeY&list=PLA0M1Bcd0w8zo9ND-7yEFjoHBg_fzaQ-B&index=3
# ООП Python 3 #3: режимы доступа - public, private, protected. Геттеры и сеттеры

class House:
    """Класс существительное с большой буквы
    x = 1 y = 1  атрибуты == данные
    def fun()  - методы == функции
    """

    def __init__(self, x=0, y=0, a=0, b=0):
        """открытые и закрытые атрибуты
        self.x   - открытые
        self.__x - закрытые
        """
        self.x = x
        self.y = y

        self.__a = a
        self.__b = b

    def setCor(self, a=0, b=0):
        """доступ к закрытым атрибутам устанавливаем значение
        проверяем причастность к типу
        """
        if (isinstance(a, int) or isinstance(a, float)) and \
                (isinstance(b, int) or isinstance(b, float)):
            self.__a = a
            self.__b = b
        else:
            print("Введите число")

    def getCor(self):
        """Возвращение картежа закрытых атрибутов"""
        return self.__a, self.__b


h1 = House(10, 20)
print(h1.x, h1.y)

h2 = House()
h2.setCor(4, "q")
print(h2.getCor())
