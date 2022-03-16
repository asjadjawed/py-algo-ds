def recursive_count(arr):
    if arr is None:
        return None
    if arr == []:
        return 0
    return 1 + recursive_count(arr[1:])
