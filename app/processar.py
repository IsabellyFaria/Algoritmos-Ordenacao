import csv
import app.QuickSort as QuickSort
import app.BubbleSort as BubbleSort
import app.SelectionSort as SelectionSort
import app.MergeSort as MergeSort


def processar(nome_lista,ordenacao,indice, file_folder):
    lista_usuario = []
    
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
                
    ordenar(ordenacao,lista_usuario,indice)
             
    with open(file_folder, 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(cabecalho)
        writer.writerows(lista_usuario)            
                
def ordenar(selecao,lista_usuario,indice):
    match selecao:
        case "Q":
            QuickSort.QuickSort(lista_usuario, key_index=indice)
        case "B":
            BubbleSort.BubbleSort(lista_usuario, key_index=indice)
        case "S":
            SelectionSort.SelectionSort(lista_usuario, key_index=indice)
        case "M":
            MergeSort.MergeSort(lista_usuario, key_index=indice)
    