def binary_search(list, item):
    if item is None:
        return None

    if len(list) == 0:
        return None

    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


def binary_search_recursive(list, item, low=0, high=None):
    if len(list) == 0:
        return None

    if item is None:
        return None

    if high is None:
        high = len(list) - 1

    mid = (high + low) // 2
    guess = list[mid]

    if item == guess:
        return mid
    if high < low:
        return None
    if item < guess:
        return binary_search_recursive(list, item, low, mid-1)
    if item > guess:
        return binary_search_recursive(list, item, mid+1, high)
