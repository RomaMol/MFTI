class NameIterator:
    """Класс итераций проверка в цикле"""

    def __init__(self, limit):
        """__num = 0 -- начало счета и __lim = переданный лимит до которого считать"""
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


class Persona:
    """Класс сохранения """

    def __init__(self, name, year, last_name):
        """свойство создание локальных переменных == атрибутов == данных """

        self.__name = name
        self.__year = year
        self.__last_name = last_name
        self.__persona = {}

    @property
    def name(self):
        """свойство возвращает name"""
        return self.__name

    @property
    def year(self):
        """свойство возвращает year"""
        return self.__year

    @property
    def last_name(self):
        """свойство возвращает last_name"""
        return self.__last_name


    def __iter__(self):
        return NameIterator(person)


# person1 = Persona("a1", 12, "a12")
# person2 = Persona("a2", 22, "a22")
# person3 = Persona("a3", 32, "a32")
# person4 = Persona("a4", 42, "a42")
person = Persona(10, 10, 10)
print(f'person.name {person.name} \nperson.year {person.year} \nperson.last_name {person.last_name}')
p1 = person["a4", 42, "a42"]
# img[3, 3] = "*"
# img[4, 4] = "*"
# img[5, 5] = "*"
#
#
# for i in person1:
#     print(i.name, i.year, i.last_name)
