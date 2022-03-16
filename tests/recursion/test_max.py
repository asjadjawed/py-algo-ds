import unittest
from src.recursion.max import recursive_max


class TestMax(unittest.TestCase):

    def test_none(self):
        '''Testing None'''
        self.assertEqual(recursive_max(None), None)

    def test_zero(self):
        '''Testing Empty Array'''
        self.assertEqual(recursive_max([]), None)

    def test_one(self):
        '''Max of single element array'''
        self.assertEqual(recursive_max([5]), 5)

    def test_three(self):
        '''A sum of random numbers'''
        self.assertEqual(recursive_max([2, 4, 6554, 2, -1]), 6554)


if __name__ == "__main__":
    unittest.main()
