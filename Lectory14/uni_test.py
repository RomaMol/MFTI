import unittest

from Lectory14.fib import fib


class TestFib(unittest.TestCase):

    def test_simpl(self):
        test_list = [(0, 0), (1, 1), (2, 1), (5, 5),]
        for param, result in test_list:
            self.assertEqual(fib(param), result)
            print('fib(param), result',fib(param), result)

    def test_stress(self):
        self.assertEqual(fib(30), fib(29) + fib(28))
        with self.assertRaises(ValueError):
            fib(30)

    def test_negative(self):
        with self.assertRaises(ValueError):
            fib(-1)
        with self.assertRaises(ValueError):
            fib(-100)


    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            fib(5.3)
        with self.assertRaises(TypeError):
            fib("STROKA")


if __name__ == '__main__':
    unittest.main()
