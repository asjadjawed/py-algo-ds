def recursive_sum(arr):
    if arr is None:
        return None
    if len(arr) == 0:
        return 0
    else:
        return arr[0] + recursive_sum(arr[1:])
