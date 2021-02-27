#  https://www.youtube.com/watch?v=eHnkiDQO3lc&list=PLA0M1Bcd0w8zo9ND-7yEFjoHBg_fzaQ-B&index=9
#  ООП Python 3 #9: перегрузка операторов: __add__, __iadd__, __getitem__, __setitem__ и другие

#  Как это будет в деталях работать, я думаю, вы уже догадались.
#  По аналогии могут быть перегружены и другие подобные операторы. Вот их краткий список:
#
# Оператор     Метод оператора             Оператор     Метод оператора
# x+y          __add__(self, other)        x += y       __iadd__(self, other)
# x-y          __sub__(self, other)        x -= y       __isub__(self, other)
# x*y          __mul__(self, other)        x *= y       __imul__(self, other)
# x/y          __truediv__(self, other)    x /= y       __itruediv__(self, other)
# x//y         __floordiv__(self, other)   x //= y      __ifloordiv__(self, other)
# x % y        __mod__(self, other)        x %= y       __imod__(self, other)



class Clock:
    __DAY = 86400  # число секунд в сутках

    def __init__(self, secs: int):
        if not isinstance(secs, int):
            raise ValueError("Секунды должны быть целым числлом")

        self.__secs = secs % self.__DAY

    def get_format(self):
        s = self.__secs % 60  # секунды
        m = (self.__secs // 60) % 60  # минуты
        h = int((self.__secs // 3600) % 24)  # часы
        return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"

    @classmethod
    def __get_form(cls, x):
        return str(x) if x > 9 else "0" + str(x)

    def get_seconds(self):
        return self.__secs

    def __iadd__(self, other):
        """Переопределение методя для операции сложения  c1+=c2
            self --> c1 , other ---> c2
        """
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом clock")
        self.__secs += other.get_seconds()
        return self

    def __add__(self, other):
        """Переопределение методя для операции сложения  c3 = c1+c2
            self --> c1 , other ---> c2
        """
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом clock")
        return Clock(self.__secs + other.get_seconds())

    def __eq__(self, other):
        """Переопределение методя для операции сравнения """
        return self.__secs == other.get_seconds()


c1 = Clock(100)
print(c1.get_format())
c2 = Clock(200)
print(c2.get_format())
if c1 == c2:
    print("часы равны")
else:
    print("часы неравны")

c3 = Clock(300)
c1 += c2 + c3

print(c1.get_format())
print(c2.get_format())
print(c3.get_format())
