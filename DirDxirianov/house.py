def main():
    x, y = 400, 500
    wight, height = 200, 300
    drown_house(x, y, wight, height)


def house_fund(x, y, wight, height_fund):
    print(f'house_fund x,y, wight,height_fund    {x, y, wight, height_fund}')
    pass


def house_wall():
    pass


def house_roof():
    pass


def drown_house(x, y, wight, height):
    """
    Рисует домик
    :param x: точка  центра
    :param y: нижняя точка по высоте
    :param wight: ширина домика
    :param height: высота домика
    :return: None
    """
    print(f'drow_house(x, y, wight, height    {x, y, wight, height}')
    height_fund = int(0.1 * height)
    house_fund(x, y, wight, height_fund)
    house_wall()
    house_roof()


main()
