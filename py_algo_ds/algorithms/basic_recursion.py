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


def zip_map(keys: list[str], values: list[int]):
    """
    Creates a dictionary by pairing elements from the `keys` and `values` lists.
    The function recursively pairs the first element of `keys` with the first element of `values`,
    then proceeds with the rest of the lists.

    Args:
        keys (list): A list of keys for the dictionary.
        values (list): A list of values for the dictionary.

    Returns:
        dict: A dictionary with keys from `keys` and values from `values`.

    Examples:
        >>> zip_map(['a', 'b', 'c'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3}

        >>> zip_map([], [])
        {}

        >>> zip_map(['x', 'y'], [10, 20])
        {'x': 10, 'y': 20}

        >>> zip_map(['k1'], [100])
        {'k1': 100}

        >>> zip_map(['k1', 'k2'], [100])
        {'k1': 100}
    """
    if not len(keys) or not len(values):
        # it goes depth first to get the base case map to build
        return {}
    # this dictionary is returned from the base case first
    my_dict = zip_map(keys[1:], values[1:])
    # then it is populated after the recursive call
    my_dict[keys[0]] = values[0]
    # and step by step dict is built and returned
    return my_dict
