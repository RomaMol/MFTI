from Lec12.nero import Nero


class NetWork:

    def __init__(self, *args):
        self.__nlauer = len(args)  # ����� �����
        self.__neuros = args  # ����� �������� � ����
        self.__layers = []

        # ������� ������� ��� ������� ����
        for i in range(self.__nlauer):
            self.__layers.append([Nero([], []) for n in range(self.__neuros[i])])
