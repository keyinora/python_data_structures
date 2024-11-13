class Graph:
    def depth_first_search(self, start_vertex):
        # Create an empty visited list
        visited = []
        # Start the recursive depth-first search
        self.depth_first_search_r(visited, start_vertex)
        # Return the list of visited vertices
        return visited

    def depth_first_search_r(self, visited, current_vertex):
        # Visit the current vertex by adding it to the visited list
        if current_vertex not in visited:
            visited.append(current_vertex)

            # Get a sorted list of neighbors of the current vertex
            neighbors = sorted(self.graph.get(current_vertex, []))

            # Recursively visit each unvisited neighbor
            for neighbor in neighbors:
                if neighbor not in visited:
                    self.depth_first_search_r(visited, neighbor)

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

