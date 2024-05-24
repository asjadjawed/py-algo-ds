"""
Find integer root of a positive number n
"""


def square_root(n: int) -> int:
    """
    Computes the integer square root of a non-negative integer n.

    The integer square root of a non-negative integer n is the largest integer
    m such that m * m <= n. This function uses a binary search algorithm to
    efficiently find the integer square root.

    Args:
        n (int): The non-negative integer to find the square root of.

    Returns:
        int: The integer square root of n. If n is negative, the function returns -1.

    Examples:
        >>> square_root(0)
        0
        >>> square_root(1)
        1
        >>> square_root(4)
        2
        >>> square_root(10)
        3
        >>> square_root(15)
        3
        >>> square_root(26)
        5

    Notes:
        - If n is negative, the function returns -1 to indicate that the square root
        is not defined for negative numbers.
        - The function uses a binary search approach with a time complexity of O(log n).
    """
    if n < 0:
        return -1

    low, high = 0, n
    # the initial boundary is set as false
    boundary = -1

    while low <= high:
        mid = low + (high - low) // 2
        result = mid * mid

        if result == n:
            boundary = mid
            return boundary

        if result > n:
            high = mid - 1

        if result < n:
            boundary = mid
            low = mid + 1

    return boundary
