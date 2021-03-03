# https://www.youtube.com/watch?v=Yt08fz52Cj0&list=PLA0M1Bcd0w8zo9ND-7yEFjoHBg_fzaQ-B&index=1
# ООП Python 3 #1: парадигма ООП, классы, экземпляры классов, атрибуты

class House:
    """Класс существительное с большой буквы
    x = 1 y = 1  переменные класса

    """
    x = 1
    y = 1


print('__doc__', House.__doc__)  # __doc__ служебная переменная описания класса
print('__name__', House.__name__)
print('dir', dir(House))  # полный набор переменных
print('__class__', House.__class__)

# ----------------------создание экземпляра класса --------------------------------

house1 = House()  # house1 - экземпляра класса со всеми ссылками на родительский класс
print('словарь локальных переменных', house1.__dict__)  # словарь локальных переменных
house1.x = 100
print('house1.x = ', house1.x, 'house1.y = ', house1.y)
print('id house1 = ', id(house1), '\n', 'id House = ', id(House))
print('словарь локальных переменных', house1.__dict__)  # словарь локальных переменных
house1.y = 100
print('атрибуты свойства экземпляра класса ', house1.__dict__)  # атрибуты свойства класса

print(getattr(house1, "x", False))  # обращение к атрибуту класса если есть вернет значение если нет то вернет False
print(getattr(house1, "z", False))  # обращение к атрибуту класса если есть вернет значение если нет то вернет False
print(hasattr(house1, "y"))  # проверка  атрибута класса если есть вернет True

print('проверка экземпляра', isinstance(house1, House))  # проверка экземпляра на принадлежность к классу
