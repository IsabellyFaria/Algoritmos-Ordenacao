import time
import tracemalloc
import csv
import QuickSort as QuickSort
import BubbleSort as BubbleSort
import SelectionSort as SelectionSort
import MergeSort as MergeSort

def medir_algoritmo(funcao, lista, key_index=0):
    lista_teste = lista.copy()
    tracemalloc.start()
    inicio = time.perf_counter()
    funcao(lista_teste, key_index)
    fim = time.perf_counter()
    memoria_atual, pico_memoria = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    tempo = fim - inicio
    confianca = verifica_ordenacao(lista_teste, lista, key_index)
    return tempo, pico_memoria / 1024, confianca

def verifica_ordenacao(lista_teste, lista, key_index):
    lista_correta = sorted(lista, key=lambda x: x[key_index])

    if lista_teste == lista_correta:
        return "ORDENAÇÃO CORRETA"
    elif len(lista_teste) > len(lista):
        return f"LISTA COM {len(lista_teste) - len(lista)} ELEMENTOS EXTRAS"
    elif len(lista_teste) < len(lista):
        return f"LISTA COM {len(lista) - len(lista_teste)} ELEMENTOS FALTANDO"
    else:
        erros = sum(1 for i in range(len(lista_correta)) if lista_teste[i] != lista_correta[i])
        return f"LISTA COM {erros} ELEMENTOS FORA DE ORDEM"

# --- Leitura da lista ---
lista = []
with open('produtos_5000.csv', 'r', encoding='utf-8') as file:
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
        lista.append(linha)

# --- Execução dos algoritmos ---
cabecalho_resultado = ['ALGORITMO', 'TEMPO (s)', 'MEMÓRIA (KB)', 'CONFIABILIDADE']
linhas = [
    ['Bubble Sort'],
    ['Selection Sort'],
    ['Merge Sort'],
    ['Quick Sort']
]

# Bubble Sort
b_tempo, b_memoria, b_confianca = medir_algoritmo(BubbleSort.BubbleSort, lista, 3)
linhas[0].extend([b_tempo, b_memoria, b_confianca])

# Selection Sort
s_tempo, s_memoria, s_confianca = medir_algoritmo(SelectionSort.SelectionSort, lista, 3)
linhas[1].extend([s_tempo, s_memoria, s_confianca])

# Merge Sort
m_tempo, m_memoria, m_confianca = medir_algoritmo(MergeSort.MergeSort, lista, 3)
linhas[2].extend([m_tempo, m_memoria, m_confianca])

# Quick Sort
q_tempo, q_memoria, q_confianca = medir_algoritmo(QuickSort.QuickSort, lista, 3)
linhas[3].extend([q_tempo, q_memoria, q_confianca])

# --- Salva resultados ---
with open('resultados_comparacao.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(cabecalho_resultado)
    writer.writerows(linhas)

print("\n✅ Resultados salvos em 'resultados_comparacao.csv'")
