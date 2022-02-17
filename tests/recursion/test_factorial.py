import unittest
from src.recursion.factorial import factorial


class TestFactorial(unittest.TestCase):

    def test_none(self):
        '''A factorial of none'''
        self.assertEqual(factorial(None), None)

    def test_zero(self):
        '''A factorial of 0'''
        self.assertEqual(factorial(0), 0)

    def test_one(self):
        '''A factorial of one'''
        self.assertEqual(factorial(1), 1)

    def test_five(self):
        '''A factorial of 5'''
        self.assertEqual(factorial(5), 120)


if __name__ == "__main__":
    unittest.main()
