"""
Simple recursive functions
"""


def count_forward_rec(n: int) -> None:
    """
    Print numbers from 1 to n in ascending order using recursion.

    Parameters:
    n (int): The number up to which to count.

    Returns:
    None
    """
    if n == 0:
        return
    count_forward_rec(n - 1)
    print(n)


def count_backwards_rec(n: int) -> None:
    """
    Print numbers from n to 1 in descending order using recursion.

    Parameters:
    n (int): The number from which to start counting down.

    Returns:
    None
    """
    if n == 0:
        return
    print(n)
    count_backwards_rec(n - 1)


def count_items_rec(arr: list[int]) -> int:
    """
    Count the number of items in a list using recursion.

    Parameters:
    arr (list[int]): The list of items to count.

    Returns:
    int: The number of items in the list.
    """
    if len(arr) == 0:
        return 0
    return 1 + count_items_rec(arr[1:])


def sum_items_rec(arr: list[int]) -> int:
    """
    Calculate the sum of items in a list using recursion.

    Parameters:
    arr (list[int]): The list of integers to sum.

    Returns:
    int: The sum of the items in the list.
    """
    if len(arr) == 0:
        return 0
    return arr[0] + sum_items_rec(arr[1:])


def find_max_rec(arr: list[int]) -> float:
    """
    Find the maximum value in a list using recursion.

    Parameters:
    arr (list[int]): The list of integers to find the maximum in.

    Returns:
    float: The maximum value in the list. Returns float('nan') if the list is empty.
    """
    if len(arr) == 0:
        return float("nan")
    if len(arr) == 1:
        return arr[0]
    sub_max = find_max_rec(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max
