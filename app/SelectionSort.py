def SelectionSort(A, key_index=0):
    n = len(A)
    left = 0
    right = n - 1

    while left < right:
        # Encontrar mínimo e máximo em um único loop
        imin = left
        imax = left

        for i in range(left + 1, right + 1):
            key_i = A[i][key_index] if isinstance(A[i], list) else A[i]
            key_min = A[imin][key_index] if isinstance(A[imin], list) else A[imin]
            key_max = A[imax][key_index] if isinstance(A[imax], list) else A[imax]

            if key_i < key_min:
                imin = i
            elif key_i > key_max:
                imax = i

        # Troca o menor com a posição 'left'
        A[left], A[imin] = A[imin], A[left]

        # Ajuste: se o máximo estava na posição 'left', ele foi movido
        if imax == left:
            imax = imin

        # Troca o maior com a posição 'right'
        A[right], A[imax] = A[imax], A[right]

        left += 1
        right -= 1
