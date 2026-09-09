from digraph import Digraph

class DirectedDFS:

    def __init__(self, G, sources):
        self._marked = [False for _ in range(G.V)]
        self.count = 0
        for s in sources:
            s = int(s)
            if not self._marked[s]:
                self.dfs(G, s)

    def dfs(self, G, v):
        self._marked[v] = True
        self.count += 1
        for w in G.adj[v]:
            if not self._marked[w]:
                self.dfs(G, w)
