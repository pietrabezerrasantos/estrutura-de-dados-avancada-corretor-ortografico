<<<<<<< HEAD
# Corretor Ortográfico com Busca Aproximada

Projeto da disciplina de Estrutura de Dados Avançada.

## Projeto escolhido

**Projeto 6 — Corretor Ortográfico com Busca Aproximada (Fuzzy Search / Tolerância a Erros de Digitação).**

## Integrantes

- Integrante 1: preencher nome
- Integrante 2: preencher nome
- Integrante 3: preencher nome

## Estruturas e algoritmos implementados

- Trie implementada manualmente.
- Busca aproximada com DFS e backtracking.
- Distância de Levenshtein calculada incrementalmente.
- MergeSort implementado manualmente para ordenar sugestões por frequência e distância.

## Formato do arquivo de entrada

```json
{
  "max_distance": 2,
  "top_k": 5,
  "dictionary": [
    { "word": "casa", "frequency": 90 }
  ],
  "queries": ["caza"]
}
```

## Como executar

### Linux/macOS/Git Bash

```bash
chmod +x run.sh
./run.sh data/input_basico.json data/output_basico.json
```

### Windows PowerShell

```powershell
python src/main.py data/input_basico.json data/output_basico.json
```

## Gerar massa de testes

```bash
python src/generate_data.py 100 20 data/input_basico_gerado.json
python src/generate_data.py 1000 100 data/input_avancado_gerado.json
python src/generate_data.py 200000 1000 data/input_estresse.json
```

## Complexidade

- Inserção na Trie: O(N * L)
- Busca aproximada: DFS com poda por distância máxima
- Ordenação das sugestões: O(S log S)

Onde:

- N = quantidade de termos do dicionário
- L = tamanho médio das palavras
- S = quantidade de sugestões encontradas
=======
# estrutura-de-dados-avancada-corretor-ortografico
>>>>>>> 908b01bf131075547242ffa5ea634e3b4b7474aa
