"""
Test for Anagram check
"""

from py_algo_ds.problems.is_anagram import is_anagram


def test_is_anagram():
    assert is_anagram("listen", "silent") is True
    assert is_anagram("hello", "billion") is False
    assert is_anagram("anagram", "nagaram") is True
    assert is_anagram("rat", "car") is False
    assert is_anagram("", "") is True
    assert is_anagram("a", "a") is True
    assert is_anagram("a", "b") is False
