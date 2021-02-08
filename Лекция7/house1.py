def main():
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


def house_wall(x, y, height_wall, width):
    """

    :param x: точка средина фундамента домика
    :param y: нижняя точка фундамента домика
    :param height_wall: высота стен
    :param width: ширина фундамента домика
    :return:
    """
    print(f'начальные данные стен домика x, y, height_wall, width {x, y, height_wall, width}')
    pass


def house_roof(x, y, height_roof, width):
    """

    :param x: точка средина фундамента домика
    :param y: нижняя точка фундамента домика
    :param height_roof:
    :param width: ширина фундамента домика
    :return:
    """
    print(f'начальные данные roof домика x, y, height_roof, width {x, y, height_roof, width}')
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
    height_wall = int(0.80 * heigh)
    height_roof = int(0.15 * heigh)
    house_fund(x, y, height_fund, width)
    house_wall(x, y, height_wall, width)
    house_roof(x, y, height_roof, width)


if __name__ == '__main__':
    main()
