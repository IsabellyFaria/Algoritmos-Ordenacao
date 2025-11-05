def BubbleSort(lista):
    mudou = True
    n = len(lista) - 1 
    while mudou:
        mudou = False
        guarda = 0      
        j = 0
        while j < n:
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                mudou = True
                guarda = j
            j += 1
        n = guarda   
    return lista
