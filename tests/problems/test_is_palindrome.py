import pytest

from py_algo_ds.problems.is_palindrome import is_palindrome


def test_is_palindrome():
    assert is_palindrome("A man, a plan, a canal: Panama") is True
    assert is_palindrome("race a car") is False
    assert is_palindrome("") is True
    assert is_palindrome("a.") is True
    assert is_palindrome("abccba") is True
    assert is_palindrome("abc") is False


if __name__ == "__main__":
    pytest.main()
