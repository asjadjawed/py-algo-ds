def selection_sort(arr):
    if arr is None:
        return None

    if len(arr) == 1:
        return arr

    for i in range(len(arr)):
        ival = arr[i]
        smallest_index = i
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr
