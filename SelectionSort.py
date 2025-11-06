def EnhSel(A):
    A = A[:]        # cópia
    n = len(A)
    B = [None] * n

    f = 0           # front
    r = n - 1       # rear

    while f < r and n > 0:

        # ---- menor elemento ----
        imin = 0
        vmin = A[0]

        for i in range(1, n):
            if A[i] < vmin:
                vmin = A[i]
                imin = i

        B[f] = vmin
        f += 1

        # Compacta removendo o menor
        for i in range(imin, n - 1):
            A[i] = A[i + 1]
        n -= 1

        if f >= r:
            break

        # ---- maior elemento ----
        imax = 0
        vmax = A[0]

        for i in range(1, n):
            if A[i] > vmax:
                vmax = A[i]
                imax = i

        B[r] = vmax
        r -= 1

        # Compacta removendo o maior
        for i in range(imax, n - 1):
            A[i] = A[i + 1]
        n -= 1

    # Se restar 1 elemento
    if f == r and n > 0:
        B[f] = A[0]

    return B