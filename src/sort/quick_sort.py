from cmath import pi


def quick_sort(arr):
    if arr is None:
        return None
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    left = [l for l in arr[1:] if l <= pivot]
    right = [r for r in arr[1:] if r > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)
