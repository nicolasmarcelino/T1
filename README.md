# T1

**Grupo D**

# Participantes
- Nicolas Marcelino da Mota
- Gabriel Rocha da Cunha

# Problema
**Problema D: Dominoes 2**

O problema apresenta uma sequência de dominós em que alguns são derrubados manualmente. A partir deles, sua queda pode desencadear a queda de outros dominós conforme as relações estabelecidas entre eles. O objetivo é descobrir quantos dominós cairão ao todo.

Disponível em: https://open.kattis.com/problems/dominoes2


# Justificativas
**Modelagem matemática: grafo direcionado**

Nosso problema será modelado em um grafo direcionado, pois cada dominó é representado por um vértice e cada relação `(x, y)` representa uma aresta direcionada de `x` para `y`, indicando que, se `x` cair, `y` também cairá.

**Representação computacional: lista de adjacência**

Optou-se pela lista de adjacência porque o grafo tende a ser esparso, permitindo armazenar apenas as relações de queda existentes.

# Implementação
Código-fonte adaptado da tradução Python disponibilizado em [shellfly/algs4-py](https://github.com/shellfly/algs4-py) do código-fonte Java originalmente escrito pelos autores Robert Sedgewick e Kevin Wayne como parte do material disponibilizado na seção [Directed Graphs](https://algs4.cs.princeton.edu/42digraph/) do livro Algorithms.

## Alterações:
- métodos como `degree()`, `max_degree()` e `number_of_self_loops()` foram removidos da classe `Digraph`;
- substitui a implementação da _bag_ para listas nativas do Python na classe `Digraph` para mapear vizinhos de um vértice;
- adicionado um contador de vértices visitados no método `dfs()` da classe `DirectedDFS`.

# Complexidade
**Complexidade de tempo: O(V + E)**

Cada vértice é visitado no máximo uma vez e, para cada vértice visitado, suas arestas de saída são percorridas para verificar seus vizinhos.

**Complexidade de espaço: O(V)**

É necessário armazenar uma informação de visitado para cada vértice do grafo, mesmo que alguns deles não sejam alcançados pela DFS.
