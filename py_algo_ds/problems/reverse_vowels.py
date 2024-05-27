"""
2 - pointer problem for string manipulation
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
    vowels = {"a", "e", "i", "o", "u"}
    reversed_vowels = list(s)
    i, j = 0, len(reversed_vowels) - 1

    while i < j:
        while i < j and reversed_vowels[i].lower() not in vowels:
            i += 1
        while i < j and reversed_vowels[j].lower() not in vowels:
            j -= 1

        if i < j:
            reversed_vowels[i], reversed_vowels[j] = (
                reversed_vowels[j],
                reversed_vowels[i],
            )
            i += 1
            j -= 1

    return "".join(reversed_vowels)
