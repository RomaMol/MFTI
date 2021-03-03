#   https://www.youtube.com/watch?v=0zuBB1YArCQ
#   ООП Python 3 #10: собственные исключения и итерабельные объекты, методы __iter__ и __next__

class CoordError(Exception):
    """Класс вывода пользовательских  исключений"""
    pass


class MyIter:
    """Класс итераций проверка в цикле"""

    def __init__(self, limit):
        """создание локальных переменных == атрибутов == данных
        __num = 0 -- начало счета и __lim = переданный лимит до которого считать
        """
        self.__num = 0
        self.__lim = limit

    def __iter__(self):
        """проверяет и возвращеет ссылку на экземпляр class MyIter:"""
        return self

    def __next__(self):
        """сравнивает число с лимитом если меньше то +=1 и возвращает число """
        if self.__num >= self.__lim:
            raise StopIteration
        self.__num += 1
        return self.__num


class ImageXIterator:
    """Класс итераций проверка в цикле по X"""

    def __init__(self, img, y: int):
        """создание локальных переменных == атрибутов == данных
        __num = 0 -- начало счета и __lim = переданный лимит до которого считать
        """

        self.__limit = img.width
        self.__y = y
        self.__img = img
        self.__x = 0

    def __iter__(self):
        """проверяет и возвращеет ссылку на экземпляр class MyIter:"""
        return self

    def __next__(self):
        """сравнивает число с лимитом если меньше то +=1 и возвращает число """

        if self.__x >= self.__limit:
            raise StopIteration

        self.__x += 1
        #print(f'ImageXIterator  x = {self.__x}')
        return self.__img[self.__x - 1, self.__y]


class ImageYIterator:
    """Класс итераций проверка в цикле по Y"""

    def __init__(self, img):
        """создание локальных переменных == атрибутов == данных
        __y = 0 -- начало счета и __lim = переданный лимит до которого считать
        """
        print(f'ImageYIterator copy_img.width  {img.width}\n'
              f'ImageYIterator copy_img.height {img.height}')
        self.__y = 0
        self.__limit = img.height
        self.__img = img

    def __iter__(self):
        """проверяет и возвращеет ссылку на экземпляр class MyIter:"""
        return self

    def __next__(self):
        """сравнивает число с лимитом если меньше то +=1 и возвращает число """
        if self.__y >= self.__limit:
            raise StopIteration
        self.__y += 1
        #print(f'ImageYIterator  y = {self.__y}')
        return ImageXIterator(self.__img, self.__y - 1)


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

    def __iter__(self):
        return ImageYIterator(img)


# it = MyIter(10)
# for i in it:
#     print(i)

img = Image(10, 10)
print(f'ширина картинки {img.width}\nвысота картинки {img.height}')
img[3, 3] = "*"
img[4, 4] = "*"
img[5, 5] = "*"

for row in img:
    # print(f'   row =   {row}\n   img =   {img}')
    for pixel in row:
        # print(f'   pixel =   {pixel}\n   row =   {row}')
        print(pixel, sep=" ", end="")
    print()
