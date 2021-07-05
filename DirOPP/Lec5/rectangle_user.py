#   https://www.youtube.com/watch?v=77kW3F9ZBHI&list=PLA0M1Bcd0w8zo9ND-7yEFjoHBg_fzaQ-B&index=5
#   ООП Python 3 #5: статические свойства и методы классов, декоратор @staticmethod, создание синглетона

# --- создаине class rectangle--


class Rectangle_user:
    """Класс существительное с большой буквы
    x = 1 y = 1  атрибуты == данные
    def fun()  - методы == функции
    """

    width = 0
    length = 0

    def __init__(self, x=0, y=0):
        """
        данные (свойства) напрямую доступны для экземпляра cordX = x  экземпляр.cordX
        """
        Rectangle_user.length = x
        Rectangle_user.width = y

    @staticmethod  # декоратор статического метода -- нет необходимости в self
    def perimeter():
        """Rectangle perimeter  """
        perimeter = (Rectangle_user.length + Rectangle_user.width) * 2
        return perimeter

    @staticmethod  # декоратор статического метода -- нет необходимости в self
    def area():
        """Rectangle area """

        return Rectangle_user.length * Rectangle_user.width

    def area2(self):
        """Rectangle area """

        return Rectangle_user.length * Rectangle_user.width


h1 = Rectangle_user(10, 12)
# print("Введите длину прямоугольника: ", input(h1.length))
# print("Введите ширину прямоугольника: ", input(h1.width))
# print()
print("perimeter : ", h1.perimeter())
print()
print("area : ", Rectangle_user.area())
print()
print("area2 : ", Rectangle_user.area())
