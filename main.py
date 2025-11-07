import QuickSort
import BubbleSort
import SelectionSort
import MergeSort
import csv
app = True
while app:
    nome_lista = input("Digite o nome do Arquivo csv: ")

    if not nome_lista.endswith(".csv"):
        nome_lista += ".csv"

    lista_usuario = []

    with open(nome_lista, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')  # <<< separador correto!
        cabecalho = next(reader)
        for linha in reader:
            # converter colunas específicas
            linha[0] = int(linha[0])
            linha[3] = float(linha[3])  # preço é float
            linha[4] = int(linha[4])

            lista_usuario.append(linha)
    print(lista_usuario)

    print("Selecione o tipo de ordenação desejada:\n\t" \
    "1. Quick Sort\n\t2. Bubble Sort\n\t3. Selection Sort\n\t4.Merge Sort")
    selecao = int(input())
    match selecao:
        case 1:
            QuickSort.QuickSort(lista_usuario)
        case 2:
            BubbleSort.BubbleSort(lista_usuario)
        case 3:
            SelectionSort.SelectionSort(lista_usuario)
        case 4:   
            lista_usuario = MergeSort.MergeSort(lista_usuario)
    print(lista_usuario)