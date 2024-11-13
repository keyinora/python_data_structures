class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        # Add an edge from vertex u to vertex v
        if u not in self.graph:
            self.graph[u] = set()
        self.graph[u].add(v)

        # Add an edge from vertex v to vertex u (since this is an undirected graph)
        if v not in self.graph:
            self.graph[v] = set()
        self.graph[v].add(u)

    # don't touch below this line

    def edge_exists(self, u, v):
        if u in self.graph and v in self.graph:
            return (v in self.graph[u]) and (u in self.graph[v])
        return False

