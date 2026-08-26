# DFS em um grafo direcionado

A lista de adjacência abaixo representa um grafo direcionado.

```
1 -> [2]
2 -> [3, 4]
3 -> [5]
4 -> [1]
5 -> [7]
6 -> [7]
7 -> []
```

O grafo representado pela lista não é **fortemente conexo** e, por ser direcionado, não é possível visitar todos os vértices a partir de uma origem. Mesmo assim, todos os vértices estão ligados de forma que perteçam a uma só componente.

Dado um vértice inicial, é possível encontrar um caminho que leva a todos os vértices contectados a ele por meio de uma uma busca em profundidade (DFS). Para ilustrar esse algoritmo, é iniciado sua chamada pelo vértice 2.

## DFS(2)

| v | marked[] | edgeTo[v] |
|:-:|:--------:|:---------:|
| 1 |     f    |           |
| 2 |     v    |           |
| 3 |     f    |           |
| 4 |     f    |           |
| 5 |     f    |           |
| 6 |     f    |           |
| 7 |     f    |           |

Visita-se agora o primeiro vizinho listado de 2: o vértice 3.

## DFS(3)
| v | marked[] | edgeTo[v] |
|:-:|:--------:|:---------:|
| 1 |     f    |           |
| 2 |     v    |           |
| 3 |     v    |     2     |
| 4 |     f    |           |
| 5 |     f    |           |
| 6 |     f    |           |
| 7 |     f    |           |

## DFS(5)

| v | marked[] | edgeTo[v] |
|:-:|:--------:|:---------:|
| 1 |     f    |           |
| 2 |     v    |           |
| 3 |     v    |     2     |
| 4 |     f    |           |
| 5 |     v    |     3     |
| 6 |     f    |           |
| 7 |     f    |           |

## DFS(7)

| v | marked[] | edgeTo[v] |
|:-:|:--------:|:---------:|
| 1 |     f    |           |
| 2 |     v    |           |
| 3 |     v    |     2     |
| 4 |     f    |           |
| 5 |     v    |     3     |
| 6 |     f    |           |
| 7 |     v    |     5     |

Neste ponto, o algoritmo retorna alguns vértices na pilha de recursão, pois 7 não tem vizinhos, mas o vértice 5 não tem mais vizinhos a serem visitados. O vértice 3 também não. O algoritmo, então, retorna ao vértice 2 e visita o vértice 4.

## DFS(4)
| v | marked[] | edgeTo[v] |
|:-:|:--------:|:---------:|
| 1 |     f    |           |
| 2 |     v    |           |
| 3 |     v    |     2     |
| 4 |     v    |     2     |
| 5 |     v    |     3     |
| 6 |     f    |           |
| 7 |     v    |     5     |

## DFS(1)
| v | marked[] | edgeTo[v] |
|:-:|:--------:|:---------:|
| 1 |     v    |     4     |
| 2 |     v    |           |
| 3 |     v    |     2     |
| 4 |     v    |     2     |
| 5 |     v    |     3     |
| 6 |     f    |           |
| 7 |     v    |     5     |

Neste ponto, o algoritmo não pode prosseguir, pois o único vizinho de 1 especificado na lista de adjacência é o 2, a origem, já visitada. O algoritmo retorna do vértice 4 para o 2 e finaliza sua execução.

É possível constatar a propriedade fracamente conexa do grafo ao verificar a tabela do caminho percorrido, mostrando que não foi possível alcançar o vértice 6.

**Referência:** a descrição e a aplicação do algoritmo DFS apresentadas neste documento foi baseada no material [A3_BFS_DFS.pdf](https://github.com/carubbi/RPG/blob/main/mat-didatico/aulas/A3_BFS_DFS.pdf), do professor Ricardo Carubbi, que utiliza como referência o livro *Algorithms*, de Robert Sedgewick e Kevin Wayne.
