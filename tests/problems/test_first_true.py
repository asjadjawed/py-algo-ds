"""
Tests for find first true
"""

import pytest

from py_algo_ds.problems.first_true import find_boundary


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
