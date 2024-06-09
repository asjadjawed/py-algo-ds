"""
Sorting Algorithms
"""


def insertion_sort(arr: list[int]) -> list[int]:
    """
    Sorts a list of integers using the insertion sort algorithm.

    Insertion sort is a simple sorting algorithm that builds the final sorted array (or list) one item at a time.
    It is much less efficient on large lists than more advanced algorithms such as quicksort, or merge sort.
    As an example think of manually sorting playing cards.

    Args:
        arr (list[int]): A list of integers to be sorted.

    Returns:
        list[int]: The sorted list of integers.

    Example:
        >>> insertion_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
        [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

        >>> insertion_sort([10, 3, 2, 8, 6, 7, 5])
        [2, 3, 5, 6, 7, 8, 10]
    """
    for i in range(len(arr)):
        curr = i
        # gets the smallest element and inserts it at current index
        while curr > 0 and arr[curr] < arr[curr - 1]:
            # swaps current smaller element with the element before it
            arr[curr], arr[curr - 1] = arr[curr - 1], arr[curr]
            curr -= 1
    return arr


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
        swapped = False
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def quicksort(arr: list[int]):
    """
    Sorts an array using the Quicksort algorithm.

    Quicksort is a divide-and-conquer algorithm that works by selecting a 'pivot' element from the array
    and partitioning the other elements into two sub-arrays, according to whether they are less than or
    greater than the pivot. The sub-arrays are then sorted recursively.

    Parameters:
    arr (list): The list of elements to be sorted.

    Returns:
    list: A new sorted list containing the same elements as `arr`.

    Example:
    >>> quicksort([3, 6, 8, 10, 1, 2, 1])
    [1, 1, 2, 3, 6, 8, 10]

    >>> quicksort([])
    []

    >>> quicksort([1])
    [1]
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        # in case we have duplicate values of the pivot
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)
