"""
Tests for Binary Search algorithms (iterative and recursive)
"""

import pytest

from py_algo_ds.algorithms.binary_search import binary_search, binary_search_recursion


@pytest.mark.parametrize(
    "search_function",
    [
        binary_search,
        binary_search_recursion,
    ],
    ids=["Binary Search Iterative", "Binary Search Recursive"],
)
@pytest.mark.parametrize(
    "iterable, item, expected",
    [
        ([], 5, -1),
        ([1], 1, 0),
        ([1], 5, -1),
        ([1, 2, 3, 4, 5], 5, 4),
        ([1, 2, 3, 4, 5], 1, 0),
        ([1, 2, 3, 4, 5], 3, 2),
        ([-5, -3, -1, 0, 1, 3, 5], -5, 0),
        ([-5, -3, -1, 0, 1, 3, 5], 5, 6),
        ([-5, -3, -1, 0, 1, 3, 5], -1, 2),
        ([-5, -3, -1, 0, 1, 3, 5], 7, -1),
        (["apple", "banana", "cherry", "grape"], "cherry", 2),
    ],
)
def test_binary_search(search_function, iterable, item, expected):
    """
    Test binary search algorithms (iterative and recursive)
    """
    assert search_function(iterable, item) == expected
