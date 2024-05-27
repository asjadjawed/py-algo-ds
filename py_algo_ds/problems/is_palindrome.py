"""
Two Pointer solution for palindrome check
"""


def is_palindrome(s: str) -> bool:
    """
    Check if a given string is a palindrome, considering only alphanumeric characters and ignoring cases.

    Parameters:
    s (str): The input string to check.

    Returns:
    bool: True if the input string is a palindrome, False otherwise.

    Examples:
    >>> is_palindrome("A man, a plan, a canal: Panama")
    True
    >>> is_palindrome("race a car")
    False
    >>> is_palindrome("")
    True
    >>> is_palindrome("a.")
    True
    """
    sanitized = [char.lower() for char in s if char.isalnum()]
    i, j = 0, len(sanitized) - 1
    while i <= j:
        if sanitized[i] == sanitized[j]:
            i += 1
            j -= 1
        else:
            return False
    return True
