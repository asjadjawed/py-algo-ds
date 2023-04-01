"""
Testing Bubble Sort
"""

import pytest
from py_algo_ds.algorithms.bubble_sort import bubble_sort


def test_empty_list():
    """
    test empty list
    """
    arr = []
    bubble_sort(arr)
    assert len(arr) == 0


def test_single_element():
    """
    test single element list
    """
    arr = [42]
    bubble_sort(arr)
    assert arr == [42]


def test_multiple_elements():
    """
    test multiple element list
    """
    arr = [5, 3, 1, 4, 2]
    bubble_sort(arr)
    assert arr == [1, 2, 3, 4, 5]


def test_sorted_elements():
    """
    test sorted element list    
    """
    arr = [1, 2, 3, 4, 5]
    bubble_sort(arr)
    assert arr == [1, 2, 3, 4, 5]


def test_reverse_sorted_elements():
    """
    test reverse sorted element list    
    """
    arr = [5, 4, 3, 2, 1]
    bubble_sort(arr)
    assert arr == [1, 2, 3, 4, 5]


def test_duplicate_elements():
    """
    test duplicate element list    
    """
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    bubble_sort(arr)
    assert arr == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]


def test_mixed_data_types():
    """
    test mixed data types list
    """
    arr = [1, "two", 3]
    with pytest.raises(TypeError):
        bubble_sort(arr)
