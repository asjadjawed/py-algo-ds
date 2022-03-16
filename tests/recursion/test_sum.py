import unittest
from src.recursion.sum import recursive_sum


class TestSum(unittest.TestCase):

    def test_none(self):
        '''Testing None'''
        self.assertEqual(recursive_sum(None), None)

    def test_zero(self):
        '''Testing Empty Array'''
        self.assertEqual(recursive_sum([]), 0)

    def test_one(self):
        '''Sum of single element array'''
        self.assertEqual(recursive_sum([5]), 5)

    def test_three(self):
        '''A sum of random numbers'''
        self.assertEqual(recursive_sum([2, 4, 6]), 12)


if __name__ == "__main__":
    unittest.main()
