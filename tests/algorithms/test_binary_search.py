"""
Test Binary Search
"""

import pytest

from py_algo_ds.algorithms.binary_search import search, search_recursion


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
def test_search(iterable, item, expected):
    """
    Test binary search iterative
    """
    assert search(iterable, item) == expected


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
def test_search_recursion(iterable, item, expected):
    """
    Test binary search recursive
    """
    assert search_recursion(iterable, item) == expected
