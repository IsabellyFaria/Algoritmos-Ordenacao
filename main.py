import QuickSort
import BubbleSort
app = True
while app:
    lista_usuario = [64, 34, 25, 12, 22, 11, 90, 5]
    print("Selecione o tipo de ordenação desejada:\n\t" \
    "1. Quick Sort\n\t2. Bubble Sort\n\t3. Selection Sort\n\t4.Merge Sort")
    selecao = int(input())
    match selecao:
        case 1:
            QuickSort.QuickSort(lista_usuario)
        case 2:
            BubbleSort.BubbleSort(lista_usuario)
    print(lista_usuario)