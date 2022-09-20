"""
Linear Search
"""


def search(iterable: list, item: object) -> int:
    """
    Searches for the first occurrence of an element in a list in O(n)

    Args:
        iterable (list): The list to search
        item (object): The element to search for

    Returns:
        int: the index of the element if found else -1
    """
    for index, value in enumerate(iterable):
        if value == item:
            return index
    return -1
