from array import array
from py_algo_ds.datastructures.arrays import a, b


def test_list():
    assert a == [1, 2, 3]


def test_array():
    assert b == array('i', [1, 2, 3])
