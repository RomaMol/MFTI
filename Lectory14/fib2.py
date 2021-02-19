# тестируемый модуль функция
def fib(n):
    """
        выбрасывае исключеине TypeError если вызван неправильный тип данных
        выбрасывае исключеине ValueError если число отрицательное или больше 50
        :param n: целое число от 0 до 50
        :return: целое число
        """
    if not isinstance(n, int):
        raise TypeError("Fib fun can work only with class <int> type")
    if n < 0:
        raise ValueError("fib fun can native nomber ")
    if n > 999:
        raise ValueError("fin fun can not work if n > 1000")
    if n == 0:
        return 0

    f_2 = 0
    f_1 = 1
    for i in range(2, n + 1):
        f_1, f_2 = (f_1+f_2), f_1

    return f_1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
