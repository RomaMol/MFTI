#   https://www.youtube.com/watch?v=KlW6O-5pcuU&list=PLA0M1Bcd0w8zo9ND-7yEFjoHBg_fzaQ-B&index=12
#   ��� Python 3 #12: ��������� ���� (������ ����������)
import math


class Nero:
    """�������� ������ ������ �������"""
    def __init__(self, list_in, list_out):
        """�����������
        list_in -  ������ ������� ������  list_out  -������ ��������  ������
        ��������� � ��������� ���������  self.__in self.__out
        self.__value = 0 - ����� �������� �������� ����� ������
        """
        self.__in = list_in
        self.__out = list_out
        self.__value = 0

    @property
    def list_in(self):
        """���������� �������� ������� ������"""
        return self.__in

    @list_in.setter
    def list_in(self, lst):
        """���������� �������� ������� ������"""
        self.__in = lst

    @property
    def list_out(self):
        """���������� �������� ��������  ������"""
        return self.__out

    @list_out.setter
    def list_out(self, lst):
        """���������� �������� ��������  ������"""
        self.__out = lst

    def act(self, x):
        """������� ������� �������� ����������� �������� � """
        return 1 / (1 + math.exp(x))
