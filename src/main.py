"""
Programa principal do Corretor Ortográfico.

Responsável por:

- Ler o arquivo de entrada;
- Construir a Trie;
- Executar as buscas aproximadas;
- Ordenar as sugestões encontradas;
- Gerar o arquivo de saída.

Toda a interação ocorre via linha de comando (CLI),
conforme exigido pela especificação da atividade.
"""
import sys
from trie import Trie
from sort import merge_sort
from io_utils import load_input, save_output


def normalize_word(word):
    """
    Normaliza a palavra removendo espaços laterais
    e convertendo para letras minúsculas.
    """
    return word.strip().lower()


def build_trie(dictionary):
    """
    Constrói a Trie a partir da lista de termos do dicionário.

    Cada item do dicionário contém a palavra e sua frequência.
    """
    trie = Trie()

    for item in dictionary:
        word = normalize_word(item["word"])
        frequency = int(item["frequency"])

        if word:
            trie.insert(word, frequency)

    return trie


def process(input_path, output_path):
    """
    Executa o fluxo principal do sistema:

    1. lê o arquivo JSON de entrada;
    2. constrói a Trie;
    3. executa as consultas;
    4. ordena as sugestões com MergeSort;
    5. grava o arquivo JSON de saída.
    """
    input_data = load_input(input_path)

    dictionary = input_data["dictionary"]
    queries = input_data["queries"]
    max_distance = int(input_data.get("max_distance", 2))
    top_k = int(input_data.get("top_k", 5))

    trie = build_trie(dictionary)

    output = {
        "project": "corretor_ortografico",
        "max_distance": max_distance,
        "total_dictionary_terms": trie.total_words,
        "results": []
    }

    for query in queries:
        normalized_query = normalize_word(query)
        suggestions = trie.fuzzy_search(normalized_query, max_distance)
        ordered = merge_sort(suggestions)

        output["results"].append({
            "query": query,
            "suggestions": ordered[:top_k]
        })

    save_output(output_path, output)


def main():
    if len(sys.argv) != 3:
        print("Uso correto: python src/main.py <arquivo_entrada.json> <arquivo_saida.json>")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    process(input_path, output_path)


if __name__ == "__main__":
    main()
