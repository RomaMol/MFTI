
def main():
    """
    главный цикл программы
    :return:
    """
    helf = 100
    finish = False
    while not finish:
        print(f" Жизнь: {helf}")
        danage = int(input())
        helf = helf - danage
        print(f" danage   {helf}")
        if helf <= 0:

            finish = True
    print(f" GAME OVER")


main()
