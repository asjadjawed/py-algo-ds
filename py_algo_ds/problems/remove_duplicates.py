def remove_duplicates(nums: list[int]) -> int:
    """
    Removes duplicates from a sorted list of integers in-place.

    This function modifies the input list so that the first `k` elements
    contain the unique elements in sorted order, where `k` is the number
    of unique elements. The remaining elements beyond `k` can be ignored.

    Parameters:
    ----------
    nums : List[int]
        A list of integers sorted in non-decreasing order.

    Returns:
    -------
    int
        The number of unique elements remaining after duplicates are removed.

    Example:
    -------
    >>> nums = [0, 0, 1, 1, 1, 2, 2]
    >>> k = remove_duplicates(nums)
    >>> k
    3
    >>> nums[:k]
    [0, 1, 2]
    """
    if len(nums) < 2:
        return len(nums)
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] > nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1
