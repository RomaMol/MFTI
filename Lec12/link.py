#   https://www.youtube.com/watch?v=KlW6O-5pcuU&list=PLA0M1Bcd0w8zo9ND-7yEFjoHBg_fzaQ-B&index=12
#   ��� Python 3 #12: ��������� ���� (������ ����������)
import math


class Link:
    """�������� ����� ����� ����� ���������"""

    def __init__(self, n_in, n_out, w=0):
        """�����������
        n_in - ������� ������  n_out  - �������� ������
        ��������� � ��������� ���������  self.__in self.__out
        self.__w = 0 - �������� ��� ��� ����� 
                """
        self.__in = n_in
        self.__out = n_out
        self.__w = w

    @property
    def n_in(self):
        """���������� �������� ������� ������"""
        return self.__in

    @property
    def n_out(self):
        """���������� �������� ������� ������"""
        return self.__out

    @property
    def w(self):
        """���������� �������� ������� ������"""
        return self.__w