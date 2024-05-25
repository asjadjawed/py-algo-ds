"""
Bubble Sort
"""


def bubble_sort(arr: list[int]) -> list[int]:
    """
    Sorts an array of integers in ascending order using the bubble sort algorithm.

    The bubble sort algorithm repeatedly steps through the list, compares adjacent elements
    and swaps them if they are in the wrong order. This pass-through is repeated until the
    list is sorted.

    Args:
        arr (list[int]): The list of integers to be sorted.

    Returns:
        list[int]: The sorted list of integers in ascending order.

    Example:
        >>> arr = [64, 34, 25, 12, 22, 11, 90]
        >>> bubble_sort(arr)
        [11, 12, 22, 25, 34, 64, 90]
    """
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
