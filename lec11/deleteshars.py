#   https://www.youtube.com/watch?v=-ZY0KHGOQoY
#   ООП Python 3 #11: функторы и менеджеры контекста

class StripChars:
    """класс для удаления символов"""
    def __init__(self, chars):
        """добавим атрибуты список какие символы будем удалять chars"""
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        """ метод для функтора """
        if not isinstance(args[0], str):
            raise ValueError("Аргумент  должен быть строкой")
        return args[0].strip(self.__chars) # удаление в конце строки заданных символов

s1 = StripChars ("!@# $%^&*()./,~+-_")
print(s1(" !@!@ ООП @@Python !$%^3 #%% #11: ?? функторы !! и менеджеры контекста!~~!"))