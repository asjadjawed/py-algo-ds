def move_zeros(nums: list[int]):
    """
    Moves all zeros in the provided list to the end, while maintaining the relative
    order of non-zero elements.

    Parameters:
        nums (list[int]): The list of integers to be reordered.

    Returns:
        None: Modifies the list in-place without returning any value.

    Example:
        >>> nums = [1, 0, 2, 0, 0, 7]
        >>> move_zeros(nums)
        >>> print(nums)
        [1, 2, 7, 0, 0, 0]
    """
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
