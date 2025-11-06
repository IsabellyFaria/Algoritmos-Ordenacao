def QuickSort(lista):
    n = len(lista)
    
    # pilha de limites (equivalente ao pivs[] no Dafny)
    pivs = [0] * (n + 1)
    pivs[n] = n
    
    from_i = 0
    to_i = n
    top = n

    while n - from_i > 1:

        # caso quando o intervalo é pequeno (<=1)
        if (to_i - from_i) <= 1:
            # nada a ordenar
            from_i = to_i + 1
            top += 1
            to_i = pivs[top]
        
        else:
            # pivot = primeiro elemento do segmento
            pivot = lista[from_i]

            # particionamento equivalente a partition(a, from+1, to)
            mid = partition(lista, from_i + 1, to_i, pivot)

            # coloca o pivot no lugar correto
            lista[from_i], lista[mid - 1] = lista[mid - 1], lista[from_i]

            # atualiza pilha como o código Dafny faz
            top -= 1
            pivs[top] = mid - 1
            to_i = mid - 1


def partition(lista, inicio, fim, pivot):
    """
    Particionamento no mesmo estilo que o Dafny usa:
    elementos < pivot ficam à esquerda
    """
    i = inicio
    j = fim - 1

    while i <= j:
        while i < fim and lista[i] <= pivot:
            i += 1
        while j >= inicio and lista[j] > pivot:
            j -= 1
        if i < j:
            lista[i], lista[j] = lista[j], lista[i]

    return i