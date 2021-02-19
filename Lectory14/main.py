# Опережающее тестирование
from Lectory14 import fib


def main():
    print('OK')
    """Запуск программы"""
    n = int(input("Введите номер числа Фибоначи:  "))
    print(f'Ваше число Фибоначи:  {fib.fib(n)}')

if __name__ == '__main__':
    main()
