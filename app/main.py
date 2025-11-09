import csv
import QuickSort as QuickSort
import BubbleSort as BubbleSort
import SelectionSort as SelectionSort
import MergeSort as MergeSort

app = True

while app:
    nome_lista = input("Digite o nome do Arquivo csv: ")

    if not nome_lista.endswith(".csv"):
        nome_lista += ".csv"

    lista_usuario = []

    # Lê o CSV
    with open(nome_lista, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        cabecalho = next(reader)
        for linha in reader:
            try:
                linha[0] = int(linha[0])
                linha[3] = float(linha[3])
                linha[4] = int(linha[4])
            except (ValueError, IndexError):
                print(f"⚠️ Linha ignorada por erro de formato: {linha}")
                continue
            lista_usuario.append(linha)

    print("\nDeseja que a ordenação seja feita a partir de:")
    for i in range(len(cabecalho)):
        print(f"\t{i+1}. {cabecalho[i]}")

    indice = int(input("\nDigite o número do atributo: ")) - 1

    print("\nSelecione o tipo de ordenação desejada:")
    print("\t1. Quick Sort")
    print("\t2. Bubble Sort")
    print("\t3. Selection Sort")
    print("\t4. Merge Sort")

    selecao = int(input("\nEscolha: "))

    match selecao:
        case 1:
            QuickSort.QuickSort(lista_usuario, key_index=indice)
            print("\n✅ Lista ordenada com QuickSort:")
        case 2:
            BubbleSort.BubbleSort(lista_usuario, key_index=indice)
            print("\n✅ Lista ordenada com BubbleSort:")
        case 3:
            SelectionSort.SelectionSort(lista_usuario, key_index=indice)
            print("\n✅ Lista ordenada com SelectionSort:")
        case 4:
            MergeSort.MergeSort(lista_usuario, key_index=indice)
            print("\n✅ Lista ordenada com MergeSort:")
        case _:
            print("\n❌ Opção inválida!")

    for linha in lista_usuario:
        print(linha)

    continuar = input("\nDeseja ordenar outro arquivo? (s/n): ").lower()
    if continuar != 's':
        app = False