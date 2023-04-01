"""
Test cases for arrays, buffers, encoding
"""

from array import array as arr
from typing import Literal
import pytest

from py_algo_ds.datastructures.arrays import integer_array, buffer, byte_array, float_array


def test_integer_array():
    """
    Test case for integer array
    """
    assert isinstance(integer_array, arr)
    assert integer_array.typecode == 'i'
    assert integer_array.tolist() == [1, 2, 3]


def test_buffer():
    """
    Test case for buffer
    """
    assert isinstance(buffer, bytearray)
    assert buffer.decode("utf-8") == "Hello Python"


def test_byte_array():
    """
    Test case for byte array
    """
    assert isinstance(byte_array, arr)
    assert byte_array.typecode == 'b'
    assert byte_array.tolist() == [72, 101, 108,
                                   108, 111, 32, 80, 121, 116, 104, 111, 110]


def test_float_array():
    """
    Test case for float array
    """
    assert isinstance(float_array, arr)
    assert float_array.typecode == 'f'
    assert len(float_array) == len(buffer) // 4


@pytest.mark.parametrize("test_input,expected", [
    ("utf-8", "Hello Python"),
    ("utf-16", "效汬⁯祐桴湯"),
    ("ascii", "Hello Python")
])
def test_buffer_decode(
    test_input: Literal['utf-8', 'utf-16', 'ascii'],
    expected: Literal['Hello Python', '敨汬⁯慍浴湯', 'Hello Python']
):
    """
    Test case for buffer decode
    """
    assert buffer.decode(test_input) == expected


def test_integer_array_byteswap():
    """
    Test case for integer array byteswap
    """
    original_bytes = integer_array.tobytes()
    integer_array.byteswap()
    swapped_bytes = integer_array.tobytes()
    assert original_bytes != swapped_bytes
    integer_array.byteswap()  # Swap back to the original state
    assert original_bytes == integer_array.tobytes()
