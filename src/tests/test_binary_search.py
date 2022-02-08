import unittest
from search.binary_search import binary_search


class TestBinarySearch(unittest.TestCase):
    def test_binary_search(self):
        '''Test Binary Search'''
        self.assertEqual(binary_search([], None), None)
        self.assertEqual(binary_search([5], None), None)
        self.assertEqual(binary_search([], 5), None)
        self.assertEqual(binary_search([5], 5), 0)
        self.assertEqual(binary_search([5], 10), None)
        self.assertEqual(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6), 5)
        self.assertEqual(binary_search([1, 3, 5,  7, 9], 5), 2)
        self.assertEqual(binary_search([1, 3, 5,  7, 9], 11), None)
        self.assertEqual(binary_search([-1, 3, 5,  7, 9], -1), 0)
        self.assertEqual(binary_search([-1, 3, 5,  7, 9], -11), None)


if __name__ == "__main__":
    unittest.main()
