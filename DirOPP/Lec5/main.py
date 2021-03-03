#   https://www.youtube.com/watch?v=77kW3F9ZBHI&list=PLA0M1Bcd0w8zo9ND-7yEFjoHBg_fzaQ-B&index=5
#   ООП Python 3 #5: статические свойства и методы классов, декоратор @staticmethod, создание синглетона

# ---


class House:
    """Класс существительное с большой буквы
    x = 1 y = 1  атрибуты == данные
    def fun()  - методы == функции
    данные (свойства) напрямую доступны для экземпляра pointX = 10 h1.pointX
    """
    pointX = 0
    pointY = 20

    def __init__(self, x=0, y=0, ):
        """
        данные (свойства) напрямую доступны для экземпляра cordX = x  экземпляр.cordX
        """
        self.cordX = x
        self.cordY = y

h1 = House()
h2 = House()
print("h1.pointX = ", h1.pointX)
print("h2.pointX = ", h2.pointX)
print()
House.pointX = 10
print("h1.pointX = ", h1.pointX)
print("h2.pointX = ", h2.pointX)
print()
h1.pointX = 22
print("h1.pointX = ", h1.pointX)
print("h2.pointX = ", h2.pointX)
print()
#  ------------------------------------------------

print("h1.pointX = ", h1.pointX, "h1.cordX = ", h1.cordX, )
h1.cordX = 12
print("h1.pointX = ", h1.pointX, "h1.cordX = ", h1.cordX, )
print()

