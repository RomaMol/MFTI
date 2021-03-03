#   https://www.youtube.com/watch?v=77kW3F9ZBHI&list=PLA0M1Bcd0w8zo9ND-7yEFjoHBg_fzaQ-B&index=5
#   ООП Python 3 #5: статические свойства и методы классов, декоратор @staticmethod, создание синглетона

# ---


class House:
    """Класс существительное с большой буквы
    x = 1 y = 1  атрибуты == данные
    def fun()  - методы == функции
    данные (свойства) напрямую доступны для экземпляра pointX = 10 h1.pointX
    создание статического метода  для закрытых  данных __pointX = 0
    """
    __count = 0

    def __init__(self, x=0, ):
        """
        данные (свойства) напрямую доступны для экземпляра cordX = x  экземпляр.cordX
        """

        House.__count += 1
        self.cordX = x

    @staticmethod  # декоратор статического метода -- нет необходимости в self
    def getCount():
        "статический метод "
        return House.__count


h1 = House()
h2 = House()
h3 = House()
print("h1.__count = ", h1.getCount())

print()
print("House.getCount() = ", House.getCount())