import unittest

from Challenges.challenge4 import fibonacci_method

fib = fibonacci_method.fibonacci3


class Challenge2(unittest.TestCase):

    def setUp(self):
        self

    def tearDown(self):
        self

    # function for nth Fibonacci number

    def test_Fibonacci(self):
        self.print(fib.num)


if __name__ == '__main__':
    unittest.main()
