from enum import Enum
import pygame


class Cell(Enum):
    """Класс Клетка игрового поля"""
    VOID = 0  # Пустое поле
    CROSS = 1  # Кресстик в поле
    ZERO = 2  # Нолик в поле


class Player:
    """Класс игрока, содержит тип значков имя"""
    pass


class GameRoundManager:
    """Менеджер игры, запускает все просесы"""

    def __init__(self, player1: Player, player2: Player):
        self._players = [player1, player2]
        self.current_player = 0
        self._game_field = GameField()

    # def handle_click(self):
    #     """Главный цикл игры"""
    #
    #    if
    #         player = self._players(self.current_player)


class GameField:
    """Класс Игровое поле"""
    pass


class GameFieldView:
    """"""
    pass


class GameWindow:
    """Класс окно игры
    содержит виджет поляб менеджера игрового раунда

    """

    def __init__(self):
        # инициализация игры
        self.current_player = 0
        self._field_widget = GameFieldView()
        player1 = Player("pet", Cell.CROSS)
        player2 = Player("WAS", Cell.ZERO)

        self._game_round_manager = GameRoundManager(player1, player2)

    def mainloop(self):
        """Главный цикл игры"""
        finished = False
        while not finished:
            for event in pygame.get_events():
                if event.type == pygame.QUIT:
                    finished = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.x, event.y
                    if self._field_widget.check_cords_correct(x, y):
                        i, j = self._field_widget.get_coords(x, y)
                        self._game_round_manager.handle_click(i, j)
