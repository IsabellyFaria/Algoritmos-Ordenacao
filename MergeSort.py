def MergeSort(lista):
    tamanho = len(lista)
    sub_tamanho = 1  # tamanho inicial das sublistas a serem mescladas

    # enquanto o tamanho das sublistas for menor que o total
    while sub_tamanho < tamanho:
        # percorre pares de sublistas de tamanho 'sub_tamanho'
        for inicio in range(0, tamanho, 2 * sub_tamanho):
            meio = min(inicio + sub_tamanho, tamanho)
            fim = min(inicio + 2 * sub_tamanho, tamanho)
            # faz merge das duas metades [inicio:meio] e [meio:fim]
            mesclar_sublistas(lista, inicio, meio, fim)
        # dobra o tamanho das sublistas a cada iteração
        sub_tamanho *= 2


def mesclar_sublistas(lista, inicio, meio, fim):
    sublista_esquerda = lista[inicio:meio]
    sublista_direita = lista[meio:fim]

    indice_esquerda = indice_direita = 0
    indice_lista = inicio

    # mescla os elementos em ordem crescente
    while indice_esquerda < len(sublista_esquerda) and indice_direita < len(sublista_direita):
        if sublista_esquerda[indice_esquerda] <= sublista_direita[indice_direita]:
            lista[indice_lista] = sublista_esquerda[indice_esquerda]
            indice_esquerda += 1
        else:
            lista[indice_lista] = sublista_direita[indice_direita]
            indice_direita += 1
        indice_lista += 1

    # adiciona o que restar da sublista esquerda
    while indice_esquerda < len(sublista_esquerda):
        lista[indice_lista] = sublista_esquerda[indice_esquerda]
        indice_esquerda += 1
        indice_lista += 1

    # adiciona o que restar da sublista direita
    while indice_direita < len(sublista_direita):
        lista[indice_lista] = sublista_direita[indice_direita]
        indice_direita += 1
        indice_lista += 1