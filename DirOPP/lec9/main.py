#  https://www.youtube.com/watch?v=eHnkiDQO3lc&list=PLA0M1Bcd0w8zo9ND-7yEFjoHBg_fzaQ-B&index=9
#  ООП Python 3 #9: перегрузка операторов: __add__, __iadd__, __getitem__, __setitem__ и другие

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

    def __add__(self, other):
        """Переопределение методя для операции сложения  c3 = c1+c2
            self --> c1 , other ---> c2
        """
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом clock")
        return Clock(self.__secs + other.get_seconds())



c1 = Clock(8265)
c2 = Clock(8000)
c3 = c1+c2
c4 = c1+c2 + c3
print(c1.get_format())
print(c2.get_format())
print(c3.get_format())
print(c4.get_format())
