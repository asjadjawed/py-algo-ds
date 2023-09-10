"""
Two Number Sum:

Given an array of integers nums and an integer target,
return the two numbers such that they add up to target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.
You can return the answer in any order.
"""


def two_number_sum(array, target_sum):
    """
    Returns the numbers from the array that equal target sum

    Args:
        array (int): the array of possible values
        target_sum (_type_): target sum required

    Returns:
        _type_: _description_
    """
    cache = set()

    for num in array:
        required_value = target_sum - num
        if required_value in cache:
            return [num, required_value]
        cache.add(num)
    return None
