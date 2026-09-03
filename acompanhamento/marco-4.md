# BFS em um grafo direcionado

A lista de adjacência abaixo representa um grafo direcionado, o mesmo utilizado para aplicar o algoritmo de busca em profundidade no marco anterior.

```
1 -> [2]
2 -> [3, 4]
3 -> [5]
4 -> [1]
5 -> [7]
6 -> [7]
7 -> []
```

Dado um vértice inicial, é possível utilizar a busca em largura (BFS) para encontrar **o menor caminho, em número de arestas, entre esse vértice e todos os vértices alcançáveis a partir dele**. Para ilustrar esse algoritmo, é iniciado sua chamada pelo vértice 2.

A tabela que registra o estado de execução do algoritmo foi modificada para mostrar com clareza a ordem da fila de visita e a distância de cada vértice até a origem.

## BFS(2)
| queue | v | marked[] | edgeTo[v] | distTo[] |
|:-----:|:-:|:--------:|:---------:|:--------:|
|       | 1 |     f    |           |          |
|       | 2 |     v    |           |     0    |
|       | 3 |     v    |     2     |     1    |
|       | 4 |     v    |     2     |     1    |
|   4   | 5 |     f    |           |          |
|   3   | 6 |     f    |           |          |
|       | 7 |     f    |           |          |

## BFS(3)
| queue | v | marked[] | edgeTo[v] | distTo[] |
|:-----:|:-:|:--------:|:---------:|:--------:|
|       | 1 |     f    |           |          |
|       | 2 |     v    |           |     0    |
|       | 3 |     v    |     2     |     1    |
|   5   | 4 |     v    |     2     |     1    |
|   4   | 5 |     v    |     3     |     2    |
|       | 6 |     f    |           |          |
|       | 7 |     f    |           |          |

## BFS(4)
| queue | v | marked[] | edgeTo[v] | distTo[] |
|:-----:|:-:|:--------:|:---------:|:--------:|
|       | 1 |     v    |     4     |     2    |
|       | 2 |     v    |           |     0    |
|   1   | 3 |     v    |     2     |     1    |
|   5   | 4 |     v    |     2     |     1    |
|       | 5 |     v    |     3     |     2    |
|       | 6 |     f    |           |          |
|       | 7 |     f    |           |          |

## BFS(5)
| queue | v | marked[] | edgeTo[v] | distTo[] |
|:-----:|:-:|:--------:|:---------:|:--------:|
|       | 1 |     v    |     4     |     2    |
|   7   | 2 |     v    |           |     0    |
|   1   | 3 |     v    |     2     |     1    |
|       | 4 |     v    |     2     |     1    |
|       | 5 |     v    |     3     |     2    |
|       | 6 |     f    |           |          |
|       | 7 |     v    |     5     |     3    |

## BFS(1)
| queue | v | marked[] | edgeTo[v] | distTo[] |
|:-----:|:-:|:--------:|:---------:|:--------:|
|       | 1 |     v    |     4     |     2    |
|   7   | 2 |     v    |           |     0    |
|       | 3 |     v    |     2     |     1    |
|       | 4 |     v    |     2     |     1    |
|       | 5 |     v    |     3     |     2    |
|       | 6 |     f    |           |          |
|       | 7 |     v    |     5     |     3    |

O único vizinho do vértice 1 é o vértice 2, já visitado.

## BFS(7)
| queue | v | marked[] | edgeTo[v] | distTo[] |
|:-----:|:-:|:--------:|:---------:|:--------:|
|       | 1 |     v    |     4     |     2    |
|       | 2 |     v    |           |     0    |
|       | 3 |     v    |     2     |     1    |
|       | 4 |     v    |     2     |     1    |
|       | 5 |     v    |     3     |     2    |
|       | 6 |     f    |           |          |
|       | 7 |     v    |     5     |     3    |

O vértice 7 não aponta para nenhum outro vértice. Como a fila esvazia, o algoritmo encerra sua execução.
