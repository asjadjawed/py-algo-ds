"""
Checks Anagram
"""


def is_anagram(s: str, t: str) -> bool:
    """
    Check if two strings are anagrams of each other.

    An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
    typically using all the original letters exactly once.

    Args:
        s (str): The first string.
        t (str): The second string.

    Returns:
        bool: True if the strings are anagrams, False otherwise.

    Examples:
        >>> is_anagram("listen", "silent")
        True
        >>> is_anagram("hello", "billion")
        False
        >>> is_anagram("anagram", "nagaram")
        True
        >>> is_anagram("rat", "car")
        False
    """
    checker = 0

    for c in s:
        checker += ord(c)
    for c in t:
        checker -= ord(c)

    return checker == 0
