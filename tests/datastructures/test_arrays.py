"""
Test arrays module
"""

from array import array
from py_algo_ds.datastructures.arrays import a, b


def test_list():
    """
    test list
    """
    assert a == [1, 2, 3]


def test_array():
    """
    test array
    """
    assert b == array('i', [1, 2, 3])
