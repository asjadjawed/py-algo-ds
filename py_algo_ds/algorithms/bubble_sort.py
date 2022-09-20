"""
Bubble Sort
"""


def sort(arr: list[object]) -> list[object]:
    """
    Bubble Sort

    Args:
        iterable (list[object]): a list of objects that can be sorted

    Returns:
        list[object]: sorted list
    """
    for p_x in range(len(arr)-1, 0, -1):
        for p_y in range(0, p_x):
            if arr[p_y] > arr[p_y + 1]:
                [arr[p_y], arr[p_y + 1]] = [arr[p_y + 1], arr[p_y]]
    return arr
