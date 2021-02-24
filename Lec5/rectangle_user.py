#   https://www.youtube.com/watch?v=77kW3F9ZBHI&list=PLA0M1Bcd0w8zo9ND-7yEFjoHBg_fzaQ-B&index=5
#   ООП Python 3 #5: статические свойства и методы классов, декоратор @staticmethod, создание синглетона

# --- создаине class rectangle--


class Rectangle_user:
    """Класс существительное с большой буквы
    x = 1 y = 1  атрибуты == данные
    def fun()  - методы == функции
    """

    def __init__(self, x=None, y=None):
        """
        данные (свойства) напрямую доступны для экземпляра cordX = x  экземпляр.cordX
        """

        self.length = x
        self.width = y

    def perimeter(self):
        """Rectangle perimeter  """
        perimeter = (self.length + self.width) * 2
        return perimeter

    def area(self):
        """Rectangle area """
        return self.length * self.width


h1 = Rectangle_user(10, 12)
# print("Введите длину прямоугольника: ", input(h1.length))
# print("Введите ширину прямоугольника: ", input(h1.width))
# print()
print("perimeter : ", h1.perimeter())
print()
print("area : ", h1.area())


