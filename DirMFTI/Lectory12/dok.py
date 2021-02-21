def hyponenuse(leg1: float, leg2: float) -> float:
    """
    вычислить длину гипотенузы трехугольника
    :param leg1: len 1 ctorona treygolnica
    :param leg2: len 1 ctorona treygolnica
    :return: len hyponenuse
    """
    return (leg1 ** 2 + leg2 ** 2) ** 0.5


def hyponenuse1(leg1: float, leg2: float) -> float:
    """
    вычислить длину гипотенузы трехугольника
    :param leg1: len 1 ctorona treygolnica
    :param leg2: len 1 ctorona treygolnica
    :return: len hyponenuse
    """
    len3 = (leg1 ** 2 + leg2 ** 2) ** 0.5
    assert len3 ** 2 == leg1 ** 2 + leg2 ** 2, "proverka"
    return len3


def main():
    """Запуск программы"""
    print(f"input x,y   ")
    x, y = [float(a) for a in input().split()]
    print(f"hyponenuse   {hyponenuse(x, y)}")
    print(f"hyponenuse1  {hyponenuse1(x, y)}")


if __name__ == '__main__':
    """на случай использования как модуль"""
    main()
