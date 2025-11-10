def MergeSort(lista, key_index=0):
    n = len(lista)
    size = 1

    while size < n:
        for start in range(0, n, 2 * size):
            mid = min(start + size, n)
            end = min(start + 2 * size, n)
            merge_inplace(lista, start, mid, end, key_index)
        size *= 2
def get_key(elem, key_index):
    return elem[key_index] if isinstance(elem, list) else elem

def merge_inplace(lista, start, mid, end, key_index):
    i = start
    j = mid

    while i < j and j < end:
        if get_key(lista[i], key_index) <= get_key(lista[j], key_index):
            i += 1
        else:
            temp = lista[j]
            k = j

            while k > i:
                lista[k] = lista[k - 1]
                k -= 1

            lista[i] = temp

            i += 1
            j += 1
            mid += 1   