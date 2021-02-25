#   https://www.youtube.com/watch?v=77kW3F9ZBHI&list=PLA0M1Bcd0w8zo9ND-7yEFjoHBg_fzaQ-B&index=5
#   ООП Python 3 #5: статические свойства и методы классов, декоратор @staticmethod, создание синглетона

# --- создаине class rectangle--


class RectangleUser:
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
        RectangleUser.length = x
        RectangleUser.width = y

    @staticmethod  # декоратор статического метода -- нет необходимости в self
    def perimeter():
        """Rectangle perimeter  """
        perimeter = (RectangleUser.length + RectangleUser.width) * 2
        return perimeter

    @staticmethod  # декоратор статического метода -- нет необходимости в self
    def area():
        """Rectangle area
        обращение в статическом методе идет по имени класса
        """

        return RectangleUser.length * RectangleUser.width


h1 = RectangleUser(10, 12)
print("perimeter h1 : ", h1.perimeter())
h2 = RectangleUser(3, 3)
# print("Введите длину прямоугольника: ", input(h1.length))
# print("Введите ширину прямоугольника: ", input(h1.width))
# print()
print("perimeter h2 : ", h1.perimeter())
print()
print("area : ", RectangleUser.area())
