# Documentação Técnica — Projeto 6: Corretor Ortográfico

## 1. Projeto escolhido

O grupo escolheu o **Projeto 6 — Corretor Ortográfico com Busca Aproximada**, cujo objetivo é implementar um módulo de sugestões ortográficas com baixo consumo de memória.

## 2. Requisitos funcionais atendidos

## RF01 — Árvore Genérica / Trie

Foi implementada manualmente uma Árvore Trie para armazenamento do dicionário.

A estrutura permite que palavras com prefixos comuns compartilhem nós, reduzindo redundâncias e diminuindo o consumo de memória.

Por exemplo, as palavras:

- casa
- casaco
- casamento

compartilham o prefixo "casa", evitando armazenamento repetido.

A Trie foi implementada sem utilização de bibliotecas externas, atendendo às restrições da atividade.

### RF02 — Busca com Backtracking

A busca aproximada é feita com DFS na Trie. Durante o caminhamento, o algoritmo calcula incrementalmente a distância de Levenshtein entre a consulta e o prefixo visitado.

Se uma ramificação não puder mais gerar palavra válida com distância menor ou igual a 2, ela é podada.

### RF03 — MergeSort

As sugestões são ordenadas manualmente com MergeSort. O critério adotado é:

1. menor distância de edição;
2. maior frequência de uso;
3. ordem alfabética para desempate.

## 3. Complexidades

Considere:

- N = quantidade de palavras no dicionário;
- L = tamanho médio das palavras;
- S = número de sugestões encontradas.

### Inserção na Trie

Cada palavra é percorrida caractere por caractere.

Complexidade aproximada: **O(L)** por palavra.

Para N palavras: **O(N * L)**.

### Busca aproximada

A busca usa DFS e calcula uma linha da matriz de Levenshtein a cada nó visitado.

No pior caso, se não houver poda eficiente, pode visitar muitos nós da Trie. Porém, com distância máxima fixa em 2, a poda reduz significativamente a exploração.

### Ordenação

As sugestões são ordenadas com MergeSort.

Complexidade: **O(S log S)**.

## 4. Justificativa das estruturas

A Trie foi escolhida porque comprime prefixos comuns e reduz repetição de armazenamento textual. Isso atende ao requisito de baixo consumo de memória RAM.

A busca com backtracking é adequada porque permite percorrer possibilidades de correção sem gerar todas as combinações possíveis de palavras.

O MergeSort foi usado por possuir complexidade garantida **O(N log N)** e por atender à exigência de implementação manual de algoritmo clássico de ordenação.

## 5. Prova de carga

O arquivo de estresse deve conter:

- 200.000 termos válidos;
- 1.000 consultas com erros de digitação;
- distância máxima de edição igual a 2.

Para gerar:

```bash
python src/generate_data.py 200000 1000 data/input_estresse.json
```

Para executar:

```bash
python src/main.py data/input_estresse.json data/output_estresse.json
```
