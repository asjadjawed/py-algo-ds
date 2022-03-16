import unittest
from src.sort.quick_sort import quick_sort


class TestQuickSort(unittest.TestCase):

    def test_quick_sort_with_none(self):
        '''None Value'''
        self.assertEqual(quick_sort(None), None)

    def test_quick_sort_with_one_element_array(self):
        '''1 value array'''
        self.assertEqual(quick_sort([1]), [1])

    def test_quick_sort_with_small_array(self):
        '''3 value array'''
        self.assertEqual(quick_sort([1, 3, 2]), [1, 2, 3])

    def test_quick_sort_with_large_array(self):
        '''Large array sort'''
        self.assertEqual(quick_sort(
            [10, -1, 0, 0, 11, 10000, 2, 11, 3, 17]), [-1, 0, 0, 2, 3, 10, 11, 11, 17, 10000])

    def test_quick_sort_with_large_array(self):
        '''Large random array sort'''
        self.assertEqual(quick_sort(
            [1e-1, 2e-2, 1000, 5000, 1e15, -2e1, 0]), [-20.0, 0, 0.02, 0.1, 1000, 5000, 1000000000000000.0])


if __name__ == "__main__":
    unittest.main()
