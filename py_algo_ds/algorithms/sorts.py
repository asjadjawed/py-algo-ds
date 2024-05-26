"""
Sorting Algorithms
"""


def selection_sort(arr: list[int]) -> list[int]:
    """
    Sorts an array of integers in ascending order using the selection sort algorithm.

    The selection sort algorithm divides the input list into two parts: the sublist of items
    already sorted, which is built up from left to right at the front (left) of the list, and
    the sublist of items remaining to be sorted that occupy the rest of the list. Initially,
    the sorted sublist is empty and the unsorted sublist is the entire input list. The algorithm
    proceeds by finding the smallest (or largest, depending on the sorting order) element in the
    unsorted sublist, exchanging (swapping) it with the leftmost unsorted element (putting it in
    sorted order), and moving the sublist boundaries one element to the right.

    Args:
        arr (list[int]): The list of integers to be sorted.

    Returns:
        list[int]: The sorted list of integers in ascending order.

    Example:
        >>> arr = [64, 25, 12, 22, 11]
        >>> selection_sort(arr)
        [11, 12, 22, 25, 64]
    """
    for i in range(len(arr)):
        # Assume the minimum is the first element
        min_index = i
        # Check the rest of the array for a smaller element
        for j in range(i + 1, len(arr)):
            # Get the current minimum value and the current element
            min_value, j_value = arr[min_index], arr[j]
            # Update the minimum index if a smaller element is found
            if min_value > j_value:
                min_index = j
        # Swap the found minimum element with the first element of the unsorted sublist
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


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
