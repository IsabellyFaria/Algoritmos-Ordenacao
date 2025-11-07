def partition(arr, low, high):
    # vamos usar o último elemento como pivô
    pivot = arr[high]
    i = low - 1  # índice do "miolo" dos menores que o pivô

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # coloca o pivô na posição correta
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def QuickSort(arr):
    n = len(arr)
    # pilha de intervalos (low, high)
    stack = [(0, n - 1)]

    while stack:
        low, high = stack.pop()
        if low < high:
            p = partition(arr, low, high)

            # empilha as duas metades que ainda precisam ordenar
            # empilha primeiro a maior para reduzir altura da pilha
            if p - 1 - low > high - (p + 1):
                stack.append((low, p - 1))
                stack.append((p + 1, high))
            else:
                stack.append((p + 1, high))
                stack.append((low, p - 1))


