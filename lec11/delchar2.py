#   https://www.youtube.com/watch?v=-ZY0KHGOQoY&list=PLA0M1Bcd0w8zo9ND-7yEFjoHBg_fzaQ-B&index=11
#   ООП Python 3 #11: функторы и менеджеры контекста


def stripchars(chars):
    """будем удалять chars"""
    def stringstrip(string):
        """ метод для функтора """
        if not isinstance(string, str):
            raise ValueError("Аргумент  должен быть строкой")
        return string.strip(chars)
    return stringstrip

s1 = stripchars ("!@# $%^&*()./,~+-_")
print(s1(" !@!@ ООП @@Python !$%^3 и менеджеры контекста!~~!"))

s2 = stripchars ("!@# $%^&*()./,~+-_")
print(s2(" !@!@ ООП  контекста!~~!"))
print (f's1 = {id(s1)}\ns2 = {id(s2)}')