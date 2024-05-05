"""
Search Test
"""

import pytest
from py_algo_ds.algorithms.linear_search import search


def test_search_found():
    """
    Test search found
    """
    assert search([1, 2, 3, 4, 5], 3) == 2
    assert search(["apple", "banana", "cherry"], "banana") == 1
    assert search([1, 2, 3, 3, 4, 5], 3) == 2
    assert search(["apple", "banana", "cherry", "banana"], "banana") == 1


def test_search_not_found():
    """
    Test search not found
    """
    assert search([1, 2, 3, 4, 5], 6) == -1
    assert search(["apple", "banana", "cherry"], "orange") == -1


def test_search_empty_iterable():
    """
    Test search empty iterable
    """
    assert search([], 1) == -1
    assert search([], "banana") == -1


def test_search_none_item():
    """
    Test for None
    """
    assert search([1, 2, 3, None, 4, 5], None) == 3
    assert search(["apple", "banana", None, "cherry"], None) == 2
    assert search([1, 2, 3, 4, 5], None) == -1
    assert search(["apple", "banana", "cherry"], None) == -1


@pytest.mark.parametrize(
    "iterable, item",
    [
        (["apple", "banana", "cherry"], 1),
        ([1, 2, 3, 4, 5], "banana"),
        (["apple", "banana", "cherry"], 1.5),
        ([1, 2, 3, 4, 5], 1.5),
    ],
)
def test_search_mismatched_types(iterable, item):
    """
    Test search mismatched types
    """
    assert search(iterable, item) == -1
