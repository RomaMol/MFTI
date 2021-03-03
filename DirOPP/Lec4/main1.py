# https://www.youtube.com/watch?v=zwel95I7O88&list=PLA0M1Bcd0w8zo9ND-7yEFjoHBg_fzaQ-B&index=4
# ООП Python 3 #4: объекты свойства (property) и дескрипторы классов
# ---декораторы ---

class House:
    """Класс существительное с большой буквы
    x = 1 y = 1  атрибуты == данные
    def fun()  - методы == функции

    """

    def __init__(self, x=0, y=0, ):
        """открытые и закрытые атрибуты
        self.x   - открытые PUBLIC
        self.__x - закрытые PRIVATE
        """
        self.__x = x
        #self.__y = y

    def __checkValue(x):
        """Метод внутренней проверки  ненужен self
        доступ к внутреннему методу класса House.__checkValue(x)
        """
        if isinstance(x, int) or isinstance(x, float):
            return True
        return False

    # ---декораторы ---
    @property
    def corX(self):
        return self.__x

    @corX.setter
    def corX(self, x):
        """доступ к закрытым атрибутам устанавливаем значение
        проверяем причастность к типу
        __setCor - закрытый метод
        if House.__checkValue(x) and House.__checkValue(y):
        """

        if House.__checkValue(x):
            self.__x = x

        else:
            print("Введите число")

    @corX.getter
    def corX(self):
        """Возвращение картежа закрытых атрибутов
        __getCor - закрытый метод
        """
        return self.__x

    @corX.deleter
    def corX(self):
        """Удаление атрибута  свойства"""
        print('Удаление атрибута  свойств')
        del self.__x




h1 = House()
h1.CorX = 12  # запись значения
x = h1.CorX  # чтение значения
print(x)
del h1.CorX

print(x)
