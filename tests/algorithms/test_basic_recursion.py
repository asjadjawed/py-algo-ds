"""
Tests for simple recursive functions
"""

import math
import sys
from io import StringIO

from py_algo_ds.algorithms.basic_recursion import (
    count_backwards_rec,
    count_forward_rec,
    count_items_rec,
    find_max_rec,
    sum_items_rec,
)


# Helper functions to capture printed output
def capture_output(func, *args):
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    func(*args)
    output = sys.stdout.getvalue().strip()
    sys.stdout = old_stdout
    return output


def test_count_forward_rec():
    output = capture_output(count_forward_rec, 5)
    assert output == "1\n2\n3\n4\n5"


def test_count_backwards_rec():
    output = capture_output(count_backwards_rec, 5)
    assert output == "5\n4\n3\n2\n1"


def test_count_items_rec():
    assert count_items_rec([1, 2, 3, 4, 5]) == 5
    assert count_items_rec([]) == 0
    assert count_items_rec([42]) == 1


def test_sum_items_rec():
    assert sum_items_rec([1, 2, 4, 3, 5]) == 15
    assert sum_items_rec([]) == 0
    assert sum_items_rec([42]) == 42


def test_rec_max():
    assert find_max_rec([1, 2, 3, 4, 5]) == 5
    assert math.isnan(find_max_rec([]))
    assert find_max_rec([42]) == 42
    assert find_max_rec([-1, -2, -3, -4, -5]) == -1
