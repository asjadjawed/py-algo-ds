"""
Testing Linear Search
"""

from py_algo_ds.algorithms.linear_search import search as linear_search
from py_algo_ds.algorithms.binary_search import search as binary_search
from py_algo_ds.algorithms.binary_search import search_recursion as binary_search_recursive

search_type = [linear_search, binary_search, binary_search_recursive]


class TestSearch:
    """
    test linear search
    """

    def test_search_with_empty_list(self):
        """
        test search with empty list
        """
        for search in search_type:
            assert search([], 1) == -1

    def test_search_with_one_item(self):
        """
        test search with one item
        """
        for search in search_type:
            assert search([1], 1) == 0
            assert search([0], 1) == -1

    def test_search_with_two_items(self):
        """
        test search with two items
        """
        for search in search_type:
            assert search([1, 2], 1) == 0
            assert search([1, 2], 2) == 1
            assert search([1, 2], 3) == -1

    def test_search_with_five_items(self):
        """
        test search with five items
        """
        for search in search_type:
            assert search([1, 2, 3, 4, 5], 2) == 1
            assert search([1, 2, 3, 4, 5], 3) == 2
            assert search([1, 2, 3, 4, 5], 1) == 0
            assert search([1, 2, 3, 4, 5], 4) == 3
            assert search([1, 2, 3, 4, 5], 5) == 4
            assert search([1, 2, 3, 4, 5], 6) == -1
            assert search([1, 2, 3, 4, 5], 0) == -1
            assert search([1, 2, 3, 4, 5], -1) == -1

    def test_linear_search_with_chars(self):
        """
        test search with chars
        """
        for search in search_type:
            assert search(["a", "b", "c"], "a") == 0
            assert search(["a", "b", "c"], "b") == 1
            assert search(["a", "b", "c"], "c") == 2
            assert search(["a", "b", "c"], "d") == -1
            assert search(["a", "b", "c"], "A") == -1
            assert search(["a", "b", "c"], "B") == -1
            assert search(["a", "b", "c"], "C") == -1
