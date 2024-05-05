"""
Binary Search
"""


def search(iterable: list, item: object) -> int:
    """
    Searches for the first occurrence of an element in a list in O(log(n))

    Args:
        iterable (list): The list to search
        item (object): The element to search for

    Returns:
        int: the index of the element if found else -1
    """
    if not iterable:
        return -1

    low = 0
    high = len(iterable)
    while low < high:
        mid = (low + high) // 2
        pointer = iterable[mid]
        if pointer == item:
            return mid
        if pointer < item:
            low = mid + 1
        else:
            high = mid
    return -1


def search_recursion(iterable: list, item: object, start=None, end=None) -> int:
    """
    Searches for the first occurrence of an element in a list in O(log(n))

    Args:
        iterable (list): The list to search
        item (object): The element to search for
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

    mid = (start + end) // 2
    pointer = iterable[mid]

    if pointer == item:
        return mid

    if pointer > item:
        return search_recursion(iterable, item, start, mid - 1)

    return search_recursion(iterable, item, mid + 1, end)
