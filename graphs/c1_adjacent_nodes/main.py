class Graph:
    def adjacent_nodes(self, node):
        # Return a list of adjacent nodes if the node exists in the graph
        if node in self.graph:
            return list(self.graph[node])
        return []

    # don't touch below this line

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph:
            self.graph[u].add(v)
        else:
            self.graph[u] = {v}
        if v in self.graph:
            self.graph[v].add(u)
        else:
            self.graph[v] = {u}

