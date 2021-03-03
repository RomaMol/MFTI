# https://www.youtube.com/watch?v=7kk2gRf8Uws&list=PLA0M1Bcd0w8zo9ND-7yEFjoHBg_fzaQ-B&index=2
# ООП Python 3 #2: методы класса, параметр self, конструктор и деструктор

class House:
    """Класс существительное с большой буквы
    x = 1 y = 1  атрибуты == данные
    def fun()  - методы == функции
    """

    def __init__(self, x=0, y=0):  # метод конструктор КЛАССА
        """Создание экземпляра КЛАССА House"""
        print("Создание экземпляра КЛАССА House")
        self.x = x
        self.y = y

    def __del__(self):  # метод деструктор экземпляра КЛАССА
        """Удаление  экземпляра КЛАССА после удаления ссылок на методы класса"""
        print("Удаление  экземпляра КЛАССА" + self.__str__())

    def fun_var1(self):  # self - указание ссылка на экземпляр класс
        print('атрибуты класса ', self.__dict__)
        return self.__dict__

    def fun_var2(self, x, y):
        """ H1.fun_var2("fest", "second")
        передача в функцию атрибутов из экземпляра класса
        """
        self.a = x
        self.b = y

#  ----"""Создание экземпляра КЛАССА House"""
H1 = House()

# self - указание ссылка на экземпляр класс def fun_var1(self):
print(H1.fun_var1())
H1.x = 5
H1.y = 10
print(H1.fun_var1())

# - вызов метода класс House экземпляром H1 и передача в метод атрибутов (5, 10 )
H1.fun_var2("fest", "second")
print('H1.__dict__ ', H1.__dict__)

# - передача в метод класс House атрибутов (5, 10 ) и экземпляра класса H1
print("House.fun_var2(H1,5,10)", House.fun_var2(H1, 5, 10))
print('H1.__dict__ ', H1.__dict__)
print()

# ---  def __init__(self, x=0, y=0): """Создание экземпляра КЛАССА House"""
H2 = House()
H3 = House(5)
H4 = House(5, 10)

print(('Создание экземпляра КЛАССА House  ', H2.__dict__),
      ('Создание экземпляра КЛАССА House  ', H3.__dict__),
      ('Создание экземпляра КЛАССА House  ', H4.__dict__), sep="\n")
