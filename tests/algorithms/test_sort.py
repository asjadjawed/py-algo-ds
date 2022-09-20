"""
Testing Sorting Algorithms
"""

from random import shuffle
from py_algo_ds.algorithms.bubble_sort import sort as bubble_sort

sort_type = [bubble_sort]


class TestSort:
    """
    Test Sorting Algorithms
    """

    def test_sort_single_element_list(self):
        """
        Test sort single element list
        """
        for sort in sort_type:
            assert sort([0]) == [0]

    def test_sort_random_length(self):
        """
        sort a random list
        """
        for sort in sort_type:
            arr = list(range(10))
            shuffle(arr)
            sort(arr)
            assert arr == sorted(arr)

    def test_sort_random_characters(self):
        """
        sort a random list of characters
        """
        for sort in sort_type:
            arr = [chr(i) for i in range(97, 123)]
            shuffle(arr)
            sort(arr)
            assert arr == sorted(arr)

    def test_with_negative_numbers(self):
        """
        sort a random list of characters
        """
        for sort in sort_type:
            arr = list(range(-15, 15))
            shuffle(arr)
            sort(arr)
            assert arr == sorted(arr)
