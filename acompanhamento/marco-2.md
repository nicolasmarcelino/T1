# Caso 1 (Caso simples)
Aqui abordamos a utilização do caso teste de cadeia simples. Na imagem referenciamos a lista de adjacência, a representação em grafos do problema juntamente com uma entrada de exemplo.
![Cadeia Simples](./imgs/marco-2/cadeia-simples.png)

# Caso 2 (Caso sem arestas)
Aqui abordamos a utilização do caso teste sem arestas. Na imagem referenciamos a lista de adjacência, a representação em grafos do problema juntamente com uma entrada de exemplo.

![Sem Arestas](./imgs/marco-2/sem-arestas.png)

# Caso 3 (Caso cíclico)
Na imagem referenciamos a lista de adjacência, a representação em grafos do problema juntamente com uma entrada de exemplo.

![Ciclico](./imgs/marco-2/ciclico.png)


# Medidas estruturais

| **Métrica** | **Caso 1 (Cadeia simples)** | **Caso 2 (Sem arestas)** | **Caso 3 (Cíclico)** |
|-------------|------------------------------|--------------------------|----------------------|
| **Ordem |V|** | 3 | 5 | 4 |
| **Tamanho |E|** | 2 | 0 | 4 |
| **Grau de saída d⁺** | d⁺(1)=1, d⁺(2)=1, d⁺(3)=0 | todos = 0 | todos = 1 |
| **Grau de entrada d⁻** | d⁻(1)=0, d⁻(2)=1, d⁻(3)=1 | todos = 0 | todos = 1 |
| **Densidade ρ** | 2/(3×2) = 0,33 | 0/(5×4) = 0 | 4/(4×3) = 0,33 |
| **Tipo** | direcionado, não ponderado, acíclico | direcionado, trivial, vértices isolados | direcionado, cíclico, regular |
