# Contextualização
```O problema desenha um cenário onde uma``` **sequência de dominós** ``` enumerados de ``` **1 a n** ``` estão enfileirados para serem derrubados em sequência. Nem sempre um dominó vai conseguir derrubar o outro, então cada par (x, y) indica uma possível relação de queda entre duas peças, mas é apenas se x cair que y cairá também. Nos casos de teste, o problema informa os dominós que são derrubados manualmente, portanto, é possível serem iniciadas mais de uma sequência de queda.```

# Informações dadas
| Variaveis    | Descrição |
| -------- | ------- |
| N | Número de dominós    |
| M | Número de relações de queda informadas     |
| L    | Número de dominós que serão derrubados manualmente    |
| X, Y    | Se o domino x cair, então y irá cair também.    |
| Z    | Dominó que será derrubado manualmente por meio externo    |

Para representar essa relação, é ideal modelar o problema como um **grafo direcionado**, pois, há uma sequência. Cada vértice representando uma peça de dominó e cada aresta direcionada de x para y representando que, caso x venha a ser derrubado, y também cairá. Os dominós indicados por z são aqueles derrubados manualmente.

# Modelagem em grafo

Modelamos o problema como um grafo direcionado não ponderado.

## Vértice
- Cada vértice representa uma peça de dominó (n vértices).
## Arestas
- Cada relação de dominos que caem.
## Tipo do grafo 
- Direcionado
- Não ponderado
- Conexo

# Instância Pequena
| Entrada | Saída |
| -------- | ------- |
| 1 | 2 |
3 2 1
1 2
2 3
2

# Restrições
#### N, M, L ≤ 10.000.

# Hipotese inicial

Em termos simples, atingir os vértices (dominós) que foram empurrado manualmente e verificar se eles apontam para outro vértice (dominó).