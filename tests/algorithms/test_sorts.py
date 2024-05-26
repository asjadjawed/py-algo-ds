"""
Tests for various sorting algorithms
"""

import pytest

from py_algo_ds.algorithms.sorts import bubble_sort, selection_sort


@pytest.mark.parametrize("algorithm", [selection_sort, bubble_sort])
def test_empty_list(algorithm):
    assert algorithm([]) == []


@pytest.mark.parametrize("algorithm", [selection_sort, bubble_sort])
def test_single_element_list(algorithm):
    assert algorithm([1]) == [1]


@pytest.mark.parametrize("algorithm", [selection_sort, bubble_sort])
def test_sorted_list(algorithm):
    assert algorithm([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


@pytest.mark.parametrize("algorithm", [selection_sort, bubble_sort])
def test_reverse_sorted_list(algorithm):
    assert algorithm([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


@pytest.mark.parametrize("algorithm", [selection_sort, bubble_sort])
def test_unsorted_list(algorithm):
    assert algorithm([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [
        1,
        1,
        2,
        3,
        3,
        4,
        5,
        5,
        5,
        6,
        9,
    ]


@pytest.mark.parametrize("algorithm", [selection_sort, bubble_sort])
def test_list_with_duplicates(algorithm):
    assert algorithm([3, 3, 3, 3, 3]) == [3, 3, 3, 3, 3]


@pytest.mark.parametrize("algorithm", [selection_sort, bubble_sort])
def test_list_with_negative_numbers(algorithm):
    assert algorithm([0, -1, 3, -5, 2, -4, 1]) == [-5, -4, -1, 0, 1, 2, 3]
