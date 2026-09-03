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

# Observações sobre a alcançabilidade

Vale destacar que o vértice **6** nunca é marcado durante a execução. Isso acontece porque, embora `6` aponte para `7`, nenhum outro vértice do grafo aponta *para* `6`, ou seja, `6` é inalcançável a partir do vértice 2. Esse comportamento reforça uma característica importante tanto do BFS quanto do DFS: ambos exploram apenas o subgrafo alcançável a partir do vértice de origem.

O BFS visita cada vértice e cada aresta do subgrafo alcançável exatamente uma vez, resultando em complexidade **O(V + E)**, a mesma ordem de grandeza do DFS aplicado no marco anterior. A diferença entre os dois algoritmos não está na complexidade assintótica, e sim na **ordem de visita** e no **tipo de caminho encontrado**:

| | DFS | BFS |
|---|---|---|
| Estrutura de dados | Pilha | Fila |
| Ordem de visita | Aprofunda o quanto possível antes de retroceder | Explora por níveis (vizinhos mais próximos primeiro) |
| Caminho encontrado (`edgeTo`) | Não garante caminho mínimo | Garante o caminho com menor número de arestas |
| Uso típico | Detecção de ciclos, ordenação topológica, componentes conexas | Menor caminho em grafos não ponderados, nível/distância entre vértices |

No exemplo aplicado, ambos os algoritmos alcançam o mesmo conjunto de vértices a partir de 2 (`{2,3,4,5,1,7}`), mas a árvore de busca (`edgeTo`) resultante é diferente, já que o BFS prioriza sempre o vizinho descoberto mais cedo na fila. A figura abaixo representa a _BFS tree_ resultante:

```
     2
   ↙   ↘
  3     4
  ↓     ↓
  5     1
  ↓
  7
```


**Referência:** a descrição e a aplicação do algoritmo BFS apresentadas neste documento foi baseada no material [A3_BFS_DFS.pdf](https://github.com/carubbi/RPG/blob/main/mat-didatico/aulas/A3_BFS_DFS.pdf), do professor Ricardo Carubbi, que utiliza como referência o livro *Algorithms*, de Robert Sedgewick e Kevin Wayne.
