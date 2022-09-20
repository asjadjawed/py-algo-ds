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
    low = 0
    high = len(iterable) - 1
    while low <= high:
        mid = (low + high) // 2
        pointer = iterable[mid]
        if pointer == item:
            return mid
        if pointer > item:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def search_recursion(iterable: list, item: object, start=0) -> int:
    """
    Searches for the first occurrence of an element in a list in O(log(n))

    Args:
        iterable (list): The list to search
        item (object): The element to search for
        start (int, optional): Do not use, it is for keeping track of index. Defaults to 0.

    Returns:
        int: the index of the element if found else -1
    """
    low = 0
    high = len(iterable) - 1

    if high < low:
        return -1

    mid = (low + high) // 2
    pointer = iterable[mid]

    if pointer == item:
        return start + mid

    if pointer > item:
        return search_recursion(iterable[low:mid], item, low)

    if pointer < item:
        return search_recursion(iterable[mid+1: high+1], item, start+mid+1)

    return -1  # this is not needed just making pylint happy
