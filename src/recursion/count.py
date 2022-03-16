def recursive_count(arr):
    if arr is None:
        return None
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return 1
    return 1 + recursive_count(arr[1:])
