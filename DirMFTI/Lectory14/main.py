# Опережающее тестирование
from DirMFTI.Lectory14 import fib, fib2


def main():
    print('OK')
    """Запуск программы"""
    n = int(input("Введите номер числа Фибоначи:  "))
    print(f'Ваше число Фибоначи:  {fib.fib(n)}')
    print(f'Ваше число Фибоначи:  {fib2.fib(n)}')


if __name__ == '__main__':
    main()
