"""
Find integer root - Binary Search
"""

from py_algo_ds.problems.integer_root import square_root


def test_square_root():
    # Test cases where n is a perfect square
    assert square_root(0) == 0
    assert square_root(1) == 1
    assert square_root(4) == 2
    assert square_root(9) == 3
    assert square_root(16) == 4
    assert square_root(25) == 5

    # Test cases where n is not a perfect square
    assert square_root(2) == 1
    assert square_root(3) == 1
    assert square_root(5) == 2
    assert square_root(8) == 2
    assert square_root(10) == 3
    assert square_root(15) == 3
    assert square_root(26) == 5

    # Test larger numbers
    assert square_root(100) == 10
    assert square_root(101) == 10
    assert square_root(999) == 31
    assert square_root(1000) == 31
    assert square_root(1_000_000_000) == 31622

    # Edge cases
    assert (
        square_root(-1) == -1
    )  # Function does not handle negative numbers, but should not crash
