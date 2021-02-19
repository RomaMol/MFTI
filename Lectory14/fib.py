# тестируемый модуль функция
def fib(n):
    """
        выбрасывае исключеине TypeError если вызван неправильный тип данных
        выбрасывае исключеине ValueError если число отрицательное или больше 50
        :param n: целое число от 0 до 50
        :return: целое число
        """
    if isinstance(n, int):
        raise TypeError("Fib fun can work only with class <int> type")
    if n < 0:
        raise ValueError("fib fun can native nomber ")
    if n > 30:
        raise ValueError("fin fun can not work if n > 30")
    f = [0, 1]+[0]*(n-1)
    for i in range(2, n+1):
        f[n] = f[i-1] + f[i-2]
        return f[n]
