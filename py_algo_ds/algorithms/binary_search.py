"""
Binary Search
"""


def search(iterable: list, item: object) -> int:
    """
    Searches for the first occurrence of an element in a list in O(log(n))

    :param l: The list to search.
    :param x: The element to search for.
    :return: The index of the first occurrence of the element in the list.
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
