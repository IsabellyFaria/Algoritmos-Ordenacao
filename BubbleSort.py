def BubbleSort(lista):
    mudou = True
    n = len(lista)
    guarda = None
    while mudou:
        j = 1
        mudou = False
        while j < n:
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                mudou = True
                guarda = j
                j =j + 1
        n = guarda
    