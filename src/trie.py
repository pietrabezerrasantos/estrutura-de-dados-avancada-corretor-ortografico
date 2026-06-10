"""
Implementação manual de uma Árvore Trie.

A Trie é utilizada para armazenar o dicionário do corretor ortográfico,
permitindo que palavras com prefixos comuns compartilhem nós e reduzindo
a redundância no armazenamento.

Estrutura desenvolvida sem utilização de bibliotecas externas,
atendendo às restrições da atividade.
"""
class TrieNode:

    def __init__(self):
        self.children = []
        self.is_word = False
        self.frequency = 0


class Trie:
    """
Classe responsável pelas operações da Árvore Trie.

Principais funcionalidades:

- Inserção de palavras no dicionário;
- Busca aproximada utilizando DFS;
- Cálculo incremental da distância de Levenshtein;
- Poda de ramos que excedem a distância máxima permitida.

A combinação entre Trie e DFS reduz a quantidade de nós visitados,
melhorando o desempenho da busca.
"""

    def __init__(self):
        self.root = TrieNode()
        self.total_words = 0

    def _find_child(self, node, char):
        for child_char, child_node in node.children:
            if child_char == char:
                return child_node
        return None

    def insert(self, word, frequency):
        node = self.root

        for char in word:
            child = self._find_child(node, char)

            if child is None:
                child = TrieNode()
                node.children.append([char, child])

            node = child

        if not node.is_word:
            self.total_words += 1

        node.is_word = True
        node.frequency = frequency

    def fuzzy_search(self, query, max_distance):
        """
        Busca palavras com distância de Levenshtein <= max_distance.

        A cada nível da Trie, atualizamos uma linha da matriz de Levenshtein.
        Ramos cujo menor valor da linha ultrapassa max_distance são podados.
        """
        """
Executa busca aproximada sobre a Trie.

A busca utiliza DFS (Depth First Search) e calcula
incrementalmente a distância de Levenshtein.

Somente palavras cuja distância seja menor ou igual
ao limite especificado são retornadas.
"""
        results = []
        query = query.lower()

        initial_row = []
        for i in range(len(query) + 1):
            initial_row.append(i)

        for char, child in self.root.children:
            self._dfs(child, char, char, query, initial_row, max_distance, results)

        return results

    def _dfs(self, node, char, current_word, query, previous_row, max_distance, results):
        columns = len(query) + 1
        current_row = [previous_row[0] + 1]

        for column in range(1, columns):
            insert_cost = current_row[column - 1] + 1
            delete_cost = previous_row[column] + 1

            if query[column - 1] == char:
                replace_cost = previous_row[column - 1]
            else:
                replace_cost = previous_row[column - 1] + 1

            current_row.append(min(insert_cost, delete_cost, replace_cost))

        distance = current_row[-1]

        if node.is_word and distance <= max_distance:
            results.append({
                "word": current_word,
                "frequency": node.frequency,
                "distance": distance
            })

        if min(current_row) <= max_distance:
            for next_char, child in node.children:
                self._dfs(
                    child,
                    next_char,
                    current_word + next_char,
                    query,
                    current_row,
                    max_distance,
                    results
                )
