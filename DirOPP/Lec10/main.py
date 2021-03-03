#   https://www.youtube.com/watch?v=0zuBB1YArCQ
#   ООП Python 3 #10: собственные исключения и итерабельные объекты, методы __iter__ и __next__

class CoordError(Exception):
    pass


class Image:
    """Класс сохранения картинки"""

    def __init__(self, width, height, background="-"):
        """свойство создание локальных переменных == атрибутов == данных """
        self.__background = background
        self.__pixel = {}
        self.__width = width
        self.__height = height
        self.__colors = {self.__background}

    @property
    def width(self):
        """свойство возвращает ширину"""
        return self.__width

    @width.setter
    def width(self, width):
        """свойство устанавливает ширину"""
        self.__width = width

    @property
    def height(self):
        """свойство возвращает высоту"""
        return self.__height

    @height.setter
    def height(self, height):
        """свойство устанавливает высоту"""
        self.__height = height

    def __check_coord(self, coord):
        """Метод проверки координаты(x,y)
        1 Координата точки должна быть двумерным кортежем
        2 Значение координаты не выходит за приделы изображения
        """
        if not isinstance(coord, tuple) or len(coord) != 2:
            raise CoordError("Координата точки должна быть двумерным кортежем")
        if not (0 <= coord[0] < self.__width or not coord[1] < self.__height):
            raise CoordError("Значение координаты выходит за приделы изображения")

    def __setitem__(self, coord, color):
        """Метод в который передаем key = coord, value =color
           coord координаты(x,y) color цвет str(*)
           если цвет = фону то удаляем пиксел из кортежа
           (None) чтобы не было ошибки на случай отсутствия пиксела в кортеже
           иначе добавляем координаты в кортеж __colors -
        """
        self.__check_coord(coord)

        if color == self.__background:
            self.__pixel.pop(coord, None)
        else:
            self.__pixel[coord] = color
            self.__colors.add(color)

    def __getitem__(self, coord):
        """метод считывания координаты
            если координаты нет в кортеже  __colors то возвратить __background
        """
        self.__check_coord(coord)
        return self.__pixel.get(coord, self.__background)


img1 = Image(20, 30)
img1[10, 10] = "*"
color = img1[5, 5]
print(f'ширина картинки {img1.width}\nвысота картинки {img1.height}')
print()
img = Image(10, 10)
print(f'ширина картинки {img.width}\nвысота картинки {img.height}')
img[3, 3] = "*"
img[4, 4] = "*"
img[5, 5] = "*"

for y in range(img.height):
    for x in range(img.width):
        print(img[x, y], sep=" ", end="")
    print()
