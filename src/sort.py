"""
Implementação manual do algoritmo MergeSort.

O algoritmo é utilizado para ordenar as sugestões retornadas
pelo corretor ortográfico.

Critérios de ordenação:

1. Menor distância de Levenshtein;
2. Maior frequência de utilização;
3. Ordem alfabética.

Complexidade assintótica:

O(N log N)
"""
def compare_suggestions(a, b):
    """
    Critério determinístico:
    1. Menor distância de Levenshtein primeiro.
    2. Maior frequência primeiro.
    3. Ordem alfabética em caso de empate.
    """
    if a["distance"] != b["distance"]:
        return a["distance"] < b["distance"]

    if a["frequency"] != b["frequency"]:
        return a["frequency"] > b["frequency"]

    return a["word"] < b["word"]


def merge_sort(items):
    """
Implementa o algoritmo MergeSort de forma recursiva.

O vetor é dividido em duas metades,
que são ordenadas independentemente e
posteriormente intercaladas.

Complexidade assintótica:

O(N log N)
"""
    if len(items) <= 1:
        return items

    middle = len(items) // 2
    left = merge_sort(items[:middle])
    right = merge_sort(items[middle:])

    return merge(left, right)


def merge(left, right):
    """
Intercala duas listas previamente ordenadas.

Durante a intercalação é mantida a ordenação
determinística definida pela função
compare_suggestions().

Complexidade:

O(N)
"""
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if compare_suggestions(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result
