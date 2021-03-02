from Lec12.nero import Nero


class NetWork:

    def __init__(self, *args):
        self.__nlauer = len(args)  # число слоев
        self.__neuros = args  # число нейронов в слое
        self.__layers = []

        # Создаем нейроны для каждого слоя
        for i in range(self.__nlauer):
            self.__layers.append([Nero([], []) for n in range(self.__neuros[i])])
