def drag_helf():
    """ количество жизни у отрицательного персонажа"""
    global helf
    helf = 100


def drag_is_alive():
    """ проверка количество жизни у отрицательного
    персонажа на выход  из игры"""
    return helf > 0


def drag_get_damage(danage):
    """ отнивание у отрицательного персонажа жизни и сравнение с 0 """
    global helf
    helf -= danage
    if helf < 0:
        helf = 0


def drad_tolk():
    print(f" У меня {helf} здоровья!!  Faiting!!!")


def main():
    """
    главный цикл программы
    :return:
    """
    drag_helf()
    finish = False
    while not finish:
        drad_tolk()
        danage = int(input())
        drag_get_damage(danage)
        if not drag_is_alive():
            finish = True
    print(f" GAME OVER")


main()
