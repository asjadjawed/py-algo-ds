"""
Tests for find first true
"""

import pytest

from py_algo_ds.problems.first_true import find_boundary, first_not_smaller


def test_find_boundary():
    # Test cases where the boundary exists
    assert find_boundary([False, False, True, True, True]) == 2
    assert find_boundary([False, True, True, True, True]) == 1
    assert find_boundary([True, True, True, True, True]) == 0
    assert find_boundary([False, False, False, True, True]) == 3

    # Test cases where the boundary does not exist
    assert find_boundary([False, False, False, False]) == -1
    assert find_boundary([]) == -1

    # Edge cases
    assert find_boundary([True]) == 0
    assert find_boundary([False]) == -1


if __name__ == "__main__":
    pytest.main()


def test_first_not_smaller():
    # Test when target is present in the array
    assert first_not_smaller([1, 2, 3, 4, 5], 3) == 2
    assert first_not_smaller([1, 2, 3, 3, 3, 4, 5], 3) == 2

    # Test when target is not present in the array
    assert first_not_smaller([1, 2, 4, 5], 3) == 2
    assert first_not_smaller([1, 2, 4, 5], 0) == 0

    # Test when target is smaller than all elements in the array
    assert first_not_smaller([2, 3, 4, 5], 1) == 0

    # Test when target is larger than all elements in the array
    assert first_not_smaller([1, 2, 3, 4], 5) == -1

    # Test when array contains duplicate values
    assert first_not_smaller([1, 2, 2, 2, 3, 4, 5], 2) == 1

    # Test when the array is empty
    assert first_not_smaller([], 1) == -1

    # Additional edge cases
    assert first_not_smaller([1], 1) == 0
    assert first_not_smaller([1], 0) == 0
    assert first_not_smaller([1], 2) == -1
    assert first_not_smaller([1, 3, 3, 5, 7], 4) == 3
