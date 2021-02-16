from enum import Enum
import pygame

FPS = 60
SELL_SIZE = 50


class Cell(Enum):
    """Класс Клетка игрового поля"""
    VOID = 0  # Пустое поле
    CROSS = 1  # Кресстик в поле
    ZERO = 2  # Нолик в поле


class Player:
    """Класс игрока, содержит тип значков имя"""

    def __init__(self, name, sell_type):
        self.name = name
        self.sell_type = sell_type


class GameRoundManager:
    """Менеджер игры, запускает все просесы"""

    def __init__(self, player1: Player, player2: Player):
        self._players = [player1, player2]
        self._current_player = 0
        self.game_field = GameField()

    def handle_click(self, i, j):
        """Главный цикл игры"""
        player = self._players[self._current_player]
        # игрок делает клик на поле
        print(f"clock_hang {i, j}")


class GameField:
    """Класс Игровое поле"""

    def __init__(self):
        self.height = 3
        self.wight = 3
        self.sells = [[Cell.VOID] * self.height for i in range(self.wight)]


class GameFieldView:
    """ Отображение поля на экране  и выясняет место клика"""

    def __init__(self, field_to_obs):
        # загрузить картинки значков клеток отобразить состояние поля
        self._field = field_to_obs
        self._height = field_to_obs.height * SELL_SIZE
        self._wight = field_to_obs.wight * SELL_SIZE

    def drow_self(self):
        pass

    def check_cords_correct(self, x, y):
        return True

    def get_coords(self, x, y):
        return 0, 0


class GameWindow:
    """Класс окно игры
    содержит виджет поляб менеджера игрового раунда

    """

    def __init__(self):
        # инициализация игры pygame.init()
        pygame.init()
        # WINDOW
        self._height = 400
        self._wight = 400
        self._title = "CROSS_&_ZERO"
        self.screen = pygame.display.set_mode((self._height, self._wight))
        pygame.display.set_caption(self._title)

        player1 = Player("PET", Cell.CROSS)
        player2 = Player("WAS", Cell.ZERO)

        self._game_round_manager = GameRoundManager(player1, player2)
        self._field_widget = GameFieldView(self._game_round_manager.game_field)

    def mainloop(self):
        """Главный цикл игры"""
        finished = False
        clock = pygame.time.Clock()

        while not finished:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    finished = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.x, event.y
                    if self._field_widget.check_cords_correct(x, y):
                        i, j = self._field_widget.get_coords(x, y)
                        self._game_round_manager.handle_click(i, j)
            pygame.display.flip()
            clock.tick(FPS)

def main():
    """Запуск программы"""
    window = GameWindow()
    window.mainloop()
    print("Game OVER!!!")


if __name__ == '__main__':
    """на случай использования как модуль"""
    main()
