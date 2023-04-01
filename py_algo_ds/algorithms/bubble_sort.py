"""
Bubble Sort
"""

from typing import List


def bubble_sort(arr: List[int]) -> None:
    """
    Sorts an array of integers or strings using Bubble Sort algorithm.

    Args:
        arr (List[Union[int, str]]): A list of integers or strings to be sorted.
    """

    # Loop through the array from the end to the start
    for p_x in range(len(arr) - 1, 0, -1):
        # Loop through the array from the start to p_x
        for p_y in range(p_x):
            # If the current element is greater than the next one, swap them
            if arr[p_y] > arr[p_y + 1]:
                arr[p_y], arr[p_y + 1] = arr[p_y + 1], arr[p_y]
