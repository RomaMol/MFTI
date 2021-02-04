def zakaz():
    x, y = 400, 500
    heigh = 400
    width = 300

    house(x, y, heigh, width)


def house_fund(x, y, heigh_fund, width):
    """

    :param x: точка средина фундамента домика
    :param y: нижняя точка фундамента домика
    :param heigh_fund: высота фундамента
    :param width: ширина фундамента домика
    :return:
    """
    print(f'начальные данные фундамента домика x, y, high_fund, width {x, y, heigh_fund, width}')
    pass


def house(x, y, heigh, width):
    """

    :param x: точка средина домика
    :param y: нижняя точка домика
    :param heigh: высота домика
    :param width: ширина домика
    :return:
    """
    print(f'начальные данные x,y,height,width {x, y, heigh, width}')
    height_fund = int(0.05 * heigh)
    height_wall = int(0.80 * width)
    height_Roof = int(0.15 * width)
    house_fund(x, y, height_fund, width)


zakaz()
