# Prova de Carga — Projeto 6: Corretor Ortográfico

## Objetivo

Validar o comportamento do sistema em cenários de grande volume de dados, conforme especificado no enunciado da atividade.

## Cenário de Estresse

Foram gerados automaticamente:

* 200.000 termos válidos para compor o dicionário.
* 1.000 consultas contendo erros de digitação.
* Distância máxima de Levenshtein igual a 2.

A geração dos dados foi realizada por meio do arquivo:

```
src/generate_data.py
```

utilizando números pseudoaleatórios para criação das palavras e consultas.

## Execução

A massa de testes foi gerada através do comando:

```bash
python generate_data.py 200000 1000 ..\data\input_estresse.json
```

O processamento foi realizado por:

```bash
python main.py ..\data\input_estresse.json ..\data\output_estresse.json
```

## Resultados

Durante a execução:

* não ocorreram erros de memória;
* não ocorreram travamentos;
* os arquivos de saída foram gerados corretamente;
* o sistema respondeu às consultas com sugestões compatíveis com a distância máxima permitida.

## Estruturas Utilizadas

* Trie implementada manualmente;
* Busca em profundidade (DFS);
* Distância de Levenshtein;
* MergeSort implementado manualmente.

## Conclusão

Os testes demonstraram que a solução é capaz de processar grandes volumes de dados de forma estável, atendendo aos requisitos de eficiência e gerenciamento de memória propostos na atividade.
