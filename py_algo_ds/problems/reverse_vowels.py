"""
2 pointer problem for string manipulation
"""


def reverse_vowels(s: str) -> str:
    """
    Reverse the vowels in a given string.

    Args:
        s (str): The input string.

    Returns:
        str: The string with its vowels reversed.

    Examples:
        >>> reverseVowels("hello")
        'holle'
        >>> reverseVowels("leetcode")
        'leotcede'
        >>> reverseVowels("aA")
        'Aa'
        >>> reverseVowels(" ")
        ' '
    """
    vowels = "aeiou"
    rev_vowels = list(s)
    i, j = 0, len(rev_vowels) - 1

    while i < j:
        while i < j and rev_vowels[i].lower() not in vowels:
            i += 1
        while i < j and rev_vowels[j].lower() not in vowels:
            j -= 1

        rev_vowels[i], rev_vowels[j] = (
            rev_vowels[j],
            rev_vowels[i],
        )
        i += 1
        j -= 1

    return "".join(rev_vowels)
