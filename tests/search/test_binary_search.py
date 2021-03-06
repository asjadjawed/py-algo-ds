import unittest
from src.search.binary_search import binary_search, binary_search_recursive


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

    def test_binary_search_recursive(self):
        '''Test Binary Search Recursive'''
        self.assertEqual(binary_search_recursive([], None), None)
        self.assertEqual(binary_search_recursive([5], None), None)
        self.assertEqual(binary_search_recursive([], 5), None)
        self.assertEqual(binary_search_recursive([5], 5), 0)
        self.assertEqual(binary_search_recursive([5], 10), None)
        self.assertEqual(binary_search_recursive(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6), 5)
        self.assertEqual(binary_search_recursive([1, 3, 5,  7, 9], 5), 2)
        self.assertEqual(binary_search_recursive([1, 3, 5,  7, 9], 11), None)
        self.assertEqual(binary_search_recursive([-1, 3, 5,  7, 9], -1), 0)
        self.assertEqual(binary_search_recursive([-1, 3, 5,  7, 9], -11), None)


if __name__ == "__main__":
    unittest.main()
