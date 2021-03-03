#   https://www.youtube.com/watch?v=77kW3F9ZBHI&list=PLA0M1Bcd0w8zo9ND-7yEFjoHBg_fzaQ-B&index=5
#   ООП Python 3 #5: статические свойства и методы классов, декоратор @staticmethod, создание синглетона

# --- создаине class синглитона  который создает единственный экземпляр класса--


class House:
    """Класс существительное с большой буквы
    x = 1 y = 1  атрибуты == данные
    def fun()  - методы == функции
    """
    __count = 0
    __instance = None

    def __new__(cls, *args, **kwargs):
        """Перегруженный метод для создания единственного экземпляра
        super(House, cls).__new__(cls)  -- создали экземпляр класса
        cls.__instance == присвоили экземпляр класса
        """
        if not isinstance(cls.__instance, cls):
            cls.__instance = super(House, cls).__new__(cls)
        else:
            print("Экземпляр класса уже создан !!!")

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
print("h1 = ", h1)
print("id(h1),  id(h2), id(h3)", id(h1), id(h2), id(h3))

print()
