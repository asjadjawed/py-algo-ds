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
    count_nested_level,
    find_max_rec,
    reverse_string,
    sum_items_rec,
    zip_map,
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


def test_reverse_string_regular():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("open") == "nepo"


def test_reverse_string_single_char():
    assert reverse_string("a") == "a"


def test_reverse_string_empty():
    assert reverse_string("") == ""


def test_reverse_string_palindrome():
    assert reverse_string("madam") == "madam"
    assert reverse_string("racecar") == "racecar"


def test_zip_map_basic():
    assert zip_map(["a", "b", "c"], [1, 2, 3]) == {"a": 1, "b": 2, "c": 3}
    assert zip_map([], []) == {}
    assert zip_map(["x"], [10]) == {"x": 10}
    assert zip_map(["k1", "k2"], [100]) == {"k1": 100}
    assert zip_map(["k1"], [100, 200]) == {"k1": 100}
    assert zip_map(["a", "b"], [1, 2]) == {"a": 1, "b": 2}


def test_count_nested_levels_found():
    nested_docs = {"doc1": {"doc2": {"doc3": {}}, "doc4": {}}, "doc5": {}}
    assert count_nested_level(nested_docs, "doc3") == 3
    assert count_nested_level(nested_docs, "doc4") == 2


def test_count_nested_levels_not_found():
    nested_docs = {"doc1": {"doc2": {"doc3": {}}, "doc4": {}}, "doc5": {}}
    assert count_nested_level(nested_docs, "doc6") == -1


def test_count_nested_levels_root():
    nested_docs = {"doc1": {"doc2": {"doc3": {}}, "doc4": {}}, "doc5": {}}
    assert count_nested_level(nested_docs, "doc1") == 1
    assert count_nested_level(nested_docs, "doc5") == 1


def test_count_nested_levels_deeper_nesting():
    nested_docs = {"doc1": {"doc2": {"doc3": {"doc6": {}}}, "doc4": {}}, "doc5": {}}
    assert count_nested_level(nested_docs, "doc6") == 4
