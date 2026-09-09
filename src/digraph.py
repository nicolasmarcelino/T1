class Digraph:

    def __init__(self, v=0):
        self.V = v
        self.E = 0
        self.adj = [[] for _ in range(self.V)]

    def add_edge(self, v, w):
        v, w = int(v), int(w)
        self.adj[v].append(w)
        self.E += 1