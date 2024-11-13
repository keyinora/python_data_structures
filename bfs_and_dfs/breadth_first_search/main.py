class Graph:
    def breadth_first_search(self, v):
        visited = []  # List to keep track of visited vertices
        to_visit = []  # Queue to keep track of vertices to visit

        # Start with the given vertex
        to_visit.append(v)

        while to_visit:
            # Pop the first vertex from the to_visit list and mark it as visited
            current = to_visit.pop(0)
            if current not in visited:
                visited.append(current)

                # Get sorted neighbors of the current vertex
                neighbors = sorted(self.graph.get(current, []))
                
                # Add neighbors to the queue if they haven't been visited or already queued up
                for neighbor in neighbors:
                    if neighbor not in visited and neighbor not in to_visit:
                        to_visit.append(neighbor)

        # Return the list of visited vertices in breadth-first order
        return visited

    # don't touch below this line

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u in self.graph.keys():
            self.graph[u].add(v)
        else:
            self.graph[u] = set([v])
        if v in self.graph.keys():
            self.graph[v].add(u)
        else:
            self.graph[v] = set([u])

    def __repr__(self):
        result = ""
        for key in self.graph.keys():
            result += f"Vertex: '{key}'\n"
            for v in sorted(self.graph[key]):
                result += f"has an edge leading to --> {v} \n"
        return result
