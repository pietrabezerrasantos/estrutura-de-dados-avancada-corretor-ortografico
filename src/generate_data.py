import json
import random
import sys


SYLLABLES = [
    "ca", "sa", "do", "ra", "me", "li", "pa", "to", "ne", "fi",
    "pro", "gra", "ma", "sis", "te", "com", "pu", "ta", "dor",
    "al", "go", "rit", "mo", "da", "dos", "es", "tru", "tu", "ra"
]


def generate_word(min_parts=2, max_parts=5):
    parts = random.randint(min_parts, max_parts)
    word = ""

    for _ in range(parts):
        word += random.choice(SYLLABLES)

    return word


def make_typo(word):
    if len(word) <= 2:
        return word + "x"

    operation = random.randint(1, 3)
    index = random.randint(0, len(word) - 1)

    if operation == 1:
        # substituição
        return word[:index] + "x" + word[index + 1:]

    if operation == 2:
        # remoção
        return word[:index] + word[index + 1:]

    # inserção
    return word[:index] + "x" + word[index:]


def unique_dictionary(size):
    seen = set()
    dictionary = []

    while len(dictionary) < size:
        word = generate_word()

        if word not in seen:
            seen.add(word)
            dictionary.append({
                "word": word,
                "frequency": random.randint(1, 100000)
            })

    return dictionary


def generate_dataset(dictionary_size, query_size, output_path):
    dictionary = unique_dictionary(dictionary_size)
    queries = []

    for _ in range(query_size):
        base_word = random.choice(dictionary)["word"]
        typo = make_typo(base_word)

        # ocasionalmente aplica segundo erro para testar distância 2
        if random.random() < 0.35:
            typo = make_typo(typo)

        queries.append(typo)

    data = {
        "max_distance": 2,
        "top_k": 5,
        "dictionary": dictionary,
        "queries": queries
    }

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


def main():
    if len(sys.argv) != 4:
        print("Uso: python src/generate_data.py <qtd_palavras> <qtd_consultas> <saida.json>")
        sys.exit(1)

    dictionary_size = int(sys.argv[1])
    query_size = int(sys.argv[2])
    output_path = sys.argv[3]

    random.seed(42)
    generate_dataset(dictionary_size, query_size, output_path)


if __name__ == "__main__":
    main()
