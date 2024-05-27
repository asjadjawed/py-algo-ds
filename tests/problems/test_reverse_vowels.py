"""
Test for Reverse Vowels
"""

from py_algo_ds.problems.reverse_vowels import reverse_vowels


def test_reverse_vowels():
    assert reverse_vowels("hello") == "holle"
    assert reverse_vowels("leetcode") == "leotcede"
    assert reverse_vowels("aA") == "Aa"
    assert reverse_vowels(" ") == " "
    assert reverse_vowels("programming") == "prigrammong"
    assert reverse_vowels("beautiful") == "buiutafel"
    assert reverse_vowels("AEIOUaeiou") == "uoieaUOIEA"
    assert reverse_vowels("") == ""
    assert reverse_vowels("xyz") == "xyz"
