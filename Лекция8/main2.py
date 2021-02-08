class Dragon:
    """Класс объекта """

    def __init__(self, name):
        """ количество жизни у отрицательного персонажа"""
        self.name = name
        self.helf = 100

    def is_alive(self):
        """ проверка количество жизни у отрицательного
        персонажа на выход  из игры"""
        return self.helf > 0

    def get_damage(self, danage):
        """ отнивание у отрицательного персонажа жизни и сравнение с 0 """

        self.helf -= danage
        if self.helf < 0:
            self.helf = 0

    def tolk(self):
        print(f" Я  { self.name },У меня {self.helf} здоровья!!  Faiting!!!")


def main():
    """
    главный цикл программы
    :return:
    """
    drag = Dragon("Smog1")
    enemy_list = [Dragon("Smog1"),Dragon("Hidra")]
    #drag.helf()
    finish = False
    while not finish:

        drag.tolk()
        danage = int(input())
        drag.get_damage(danage)
        if not drag.is_alive():
            finish = True
    print(f" GAME OVER")


main()
