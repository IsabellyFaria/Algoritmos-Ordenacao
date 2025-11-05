def MergeSort(a):
    if len(a) <= 1:
        return a
    meio = len(a) // 2
    esquerda = a[:meio]
    direita = a[meio:]
    esquerda = MergeSort(esquerda)
    direita = MergeSort(direita)
    return Merge(esquerda, direita)

def Merge(esquerda, direita):
    resultado = []
    i = j = 0
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    # adiciona o que restou (caso uma das listas tenha sobrado)
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])

    return resultado
