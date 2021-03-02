#   https://www.youtube.com/watch?v=-ZY0KHGOQoY&list=PLA0M1Bcd0w8zo9ND-7yEFjoHBg_fzaQ-B&index=11
#   ООП Python 3 #11: функторы и менеджеры контекста

class Counter:
    """функтор """
    def __init__(self):
        """создаем переменную счетчика"""
        self.__counter = 0

    def __call__(self, *args, **kwargs):
        """ метод для функтора """
        self.__counter += 1
        print(f'self.__counter = {self.__counter}')
        return self.__counter


c1 = Counter()
c1()
c1()

c2 = Counter()
c2()
c2()