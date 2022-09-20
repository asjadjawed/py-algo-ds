"""
    Linear Search
    """


def search(iterable: list, item: object) -> int:
    """_summary_Searches for the first occurrence of an element in a list.

    :param l: The list to search.
    :param x: The element to search for.
    :return: The index of the first occurrence of the element in the list.
    """
    for index, value in enumerate(iterable):
        if value == item:
            return index
    return -1
