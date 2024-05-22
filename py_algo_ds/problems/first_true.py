"""
This module provides a function to find the boundary index of the first `True`
value in a sorted list of boolean values.
"""


def find_boundary(arr: list[bool]) -> int:
    """
    Finds the index of the first occurrence of `True` in a sorted list of boolean values.

    This function assumes that the list `arr` is sorted in non-decreasing order,
    meaning all `False` values come before any `True` values. It uses a binary
    search algorithm to efficiently find the boundary index where `True` values begin.

    Parameters:
    arr (list[bool]): A list of boolean values sorted in non-decreasing order.

    Returns:
    int: The index of the first `True` value in the list. If no `True` value is found,
        returns -1.

    Example:
    >>> find_boundary([False, False, True, True, True])
    2
    >>> find_boundary([False, True, True, True, True])
    1
    >>> find_boundary([False, False, False, False])
    -1
    >>> find_boundary([True, True, True, True])
    0
    """
    low, high = 0, len(arr) - 1
    boundary_index = -1

    while low <= high:
        mid = low + (high - low) // 2
        current_value = arr[mid]

        if current_value:
            boundary_index = mid
            high = mid - 1
        else:
            low = mid + 1

    return boundary_index
