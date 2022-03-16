import unittest
from src.recursion.count import recursive_count


class TestSum(unittest.TestCase):

    def test_none(self):
        '''Testing None'''
        self.assertEqual(recursive_count(None), None)

    def test_zero(self):
        '''Testing Empty Array'''
        self.assertEqual(recursive_count([]), 0)

    def test_one(self):
        '''Single element array'''
        self.assertEqual(recursive_count([5]), 1)

    def test_three(self):
        '''A random array'''
        self.assertEqual(recursive_count([2, 4, 6, 8]), 4)


if __name__ == "__main__":
    unittest.main()
