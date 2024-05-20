"""
Binary Search
"""


def search(iterable: list[int], item: int) -> int:
    """
    Searches for the first occurrence of an element in a list in O(log(n))

    Args:
        iterable (list[int]): The list to search
        item (int): The element to search for

    Returns:
        int: the index of the element if found else -1
    """
    if not iterable:
        return -1

    low, high = 0, len(iterable) - 1
    while low <= high:
        mid = low + (high - low) // 2
        pointer = iterable[mid]
        if pointer == item:
            return mid
        if pointer < item:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def search_recursion(iterable: list[int], item: int, start=None, end=None) -> int:
    """
    Searches for the first occurrence of an element in a list in O(log(n))

    Args:
        iterable (list[int]): The list to search
        item (int): The element to search for
        start (int, optional): Defaults to None. Auto-calculated.
        end (int, optional): Defaults to None. Auto-calculated.

    Returns:
        int: the index of the element if found else -1
    """
    if not iterable:
        return -1

    if start is None:
        start = 0
    if end is None:
        end = len(iterable) - 1

    if start > end:
        return -1

    mid = start + (end - start) // 2
    pointer = iterable[mid]

    if pointer == item:
        return mid

    if pointer > item:
        return search_recursion(iterable, item, start, mid - 1)

    return search_recursion(iterable, item, mid + 1, end)
