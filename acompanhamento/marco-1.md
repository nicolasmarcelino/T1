O problema desenha um cenário onde uma sequência de dominós enumerados de 1 a n estão enfileirados para serem derrubados em sequência. Nem sempre um dominó vai conseguir derrubar o outro, então cada par (x, y) indica uma possível relação de queda entre duas peças, mas é apenas se x cair que y cairá também. Nos casos de teste, o problema informa os dominós que são derrubados manualmente, portanto, é possível serem iniciadas mais de uma sequência de queda.

n = número de dominós

m = número de relações de queda informadas

l = número de dominós que serão derrubados manualmente

x y = se x cair, então y cairá também

z = um dominó que será derrubado manualmente

Para representar essa relação, é ideal modelar o problema como um **grafo direcionado**, onde cada vértice representa uma peça de dominó e cada aresta direcionada de x para y representa que, caso x caia, y também cairá. Os dominós indicados por z são aqueles derrubados manualmente e que garantem a condição da sequência.