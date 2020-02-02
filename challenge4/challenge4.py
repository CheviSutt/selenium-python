import unittest
from Challenges.challenge4 import fibonacci_method
fib_class = fibonacci_method.Fibonacci


class Challenge4(unittest.TestCase):

    # function for nth Fibonacci number

    def test_Fibonacci(self):
        val = fib_class(9)
        print(val)

    test_Fibonacci()


if __name__ == '__main__':
    unittest.main()
