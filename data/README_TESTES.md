# Corretor Ortográfico com Busca Aproximada

Projeto desenvolvido para a disciplina de **Estrutura de Dados Avançada**.

## Projeto Escolhido

**Projeto 6 — Corretor Ortográfico com Busca Aproximada (Fuzzy Search / Tolerância a Erros de Digitação)**

---

# Integrantes

* Nome da Integrante 1
* Nome da Integrante 2
* Nome da Integrante 3

---

# Objetivo

Desenvolver um corretor ortográfico capaz de sugerir palavras semelhantes a partir de consultas contendo erros de digitação, utilizando estruturas de dados e algoritmos implementados manualmente, sem uso de bibliotecas de alto nível.

---

# Requisitos Funcionais Implementados

## RF01 — Árvore Trie

Foi implementada manualmente uma Trie para armazenamento eficiente do dicionário.

A estrutura permite o compartilhamento de prefixos comuns entre palavras, reduzindo redundâncias e otimizando o consumo de memória.

---

## RF02 — Busca Aproximada

Foi implementada uma busca em profundidade (DFS) combinada com o cálculo incremental da distância de Levenshtein.

O sistema retorna palavras cuja distância de edição seja menor ou igual a 2.

---

## RF03 — Ordenação das Sugestões

As sugestões encontradas são ordenadas através do algoritmo MergeSort implementado manualmente.

Critérios utilizados:

1. Menor distância de Levenshtein.
2. Maior frequência de utilização.
3. Ordem alfabética.

---

# Estruturas de Dados Utilizadas

* Trie
* Busca em Profundidade (DFS)
* Distância de Levenshtein
* MergeSort

---

# Estrutura do Projeto

```
src/
│
├── trie.py
├── sort.py
├── io_utils.py
├── generate_data.py
└── main.py

data/
│
├── input_basico.json
├── input_avancado.json
├── input_estresse.json
├── output_basico.json
├── output_avancado.json
└── output_estresse.json

docs/
│
├── documentacao_tecnica.md
└── prova_de_carga.md

README.md
run.sh
```

---

# Execução

## Teste Básico

```bash
python main.py ..\data\input_basico.json ..\data\output_basico.json
```

## Teste Avançado

```bash
python main.py ..\data\input_avancado.json ..\data\output_avancado.json
```

## Teste de Estresse

### Gerar massa de dados

```bash
python generate_data.py 200000 1000 ..\data\input_estresse.json
```

### Executar

```bash
python main.py ..\data\input_estresse.json ..\data\output_estresse.json
```

---

# Complexidades

### Inserção na Trie

O(N · L)

onde:

* N = número de palavras;
* L = tamanho médio das palavras.

---

### Busca Aproximada

DFS com cálculo incremental da distância de Levenshtein.

---

### Ordenação

MergeSort:

O(S log S)

onde:

* S = quantidade de sugestões encontradas.

---

# Restrições

Não foram utilizadas bibliotecas de alto nível para implementação das estruturas de dados e algoritmos centrais.

Todas as estruturas foram desenvolvidas manualmente em Python.

---

# Prova de Carga

O sistema foi submetido ao cenário de estresse especificado pela atividade:

* 200.000 termos válidos;
* 1.000 consultas com erros de digitação;
* distância máxima igual a 2.

A execução foi concluída sem erros de memória e sem travamentos.
