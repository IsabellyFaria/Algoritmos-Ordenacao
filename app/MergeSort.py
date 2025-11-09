def MergeSort(lista, key_index=0):
    tamanho = len(lista)
    sub_tamanho = 1  # tamanho inicial das sublistas a serem mescladas

    while sub_tamanho < tamanho:
        for inicio in range(0, tamanho, 2 * sub_tamanho):
            meio = min(inicio + sub_tamanho, tamanho)
            fim = min(inicio + 2 * sub_tamanho, tamanho)
            mesclar_sublistas(lista, inicio, meio, fim, key_index)
        sub_tamanho *= 2


def mesclar_sublistas(lista, inicio, meio, fim, key_index):
    sublista_esquerda = lista[inicio:meio]
    sublista_direita = lista[meio:fim]

    indice_esquerda = indice_direita = 0
    indice_lista = inicio

    while indice_esquerda < len(sublista_esquerda) and indice_direita < len(sublista_direita):
        elem_esq = sublista_esquerda[indice_esquerda][key_index] if isinstance(sublista_esquerda[indice_esquerda], list) else sublista_esquerda[indice_esquerda]
        elem_dir = sublista_direita[indice_direita][key_index] if isinstance(sublista_direita[indice_direita], list) else sublista_direita[indice_direita]

        if elem_esq <= elem_dir:
            lista[indice_lista] = sublista_esquerda[indice_esquerda]
            indice_esquerda += 1
        else:
            lista[indice_lista] = sublista_direita[indice_direita]
            indice_direita += 1
        indice_lista += 1

    while indice_esquerda < len(sublista_esquerda):
        lista[indice_lista] = sublista_esquerda[indice_esquerda]
        indice_esquerda += 1
        indice_lista += 1

    while indice_direita < len(sublista_direita):
        lista[indice_lista] = sublista_direita[indice_direita]
        indice_direita += 1
        indice_lista += 1
