def QuickSort(lista, menor = 0, maior= None):
    #Determina o valor de maior se for a primeira chamada
    if maior == None:
        maior = len(lista)-1
    #Condição de recursividade e parada
    if menor < maior:
        index_pivo = Separar(lista, menor, maior)
        #Divide a lista e chama quicksort recursivamente
        QuickSort(lista, menor,index_pivo-1)
        QuickSort(lista, index_pivo+1,maior)
def Separar(lista, menor, maior):
    #O item de maior indice será ordenado
    pivo = lista[maior]
    i = menor - 1
    for j in range(menor,maior):
        if lista[j] <= pivo:
            i+=1
            lista[i], lista[j] = lista[j],lista[i]
    lista[i+1], lista[maior] = lista[maior], lista[i+1]
    return i+1