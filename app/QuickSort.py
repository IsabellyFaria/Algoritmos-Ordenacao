def partition(arr, low, high, key_index=0):
    pivot = arr[high]
    pivot_val = pivot[key_index] if isinstance(pivot, list) else pivot
    i = low - 1

    for j in range(low, high):
        val_j = arr[j][key_index] if isinstance(arr[j], list) else arr[j]
        if val_j <= pivot_val:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def QuickSort(arr, key_index=0):
    n = len(arr)
    stack = [(0, n - 1)]

    while stack:
        low, high = stack.pop()
        if low < high:
            p = partition(arr, low, high, key_index)

            if p - 1 - low > high - (p + 1):
                stack.append((low, p - 1))
                stack.append((p + 1, high))
            else:
                stack.append((p + 1, high))
                stack.append((low, p - 1))
