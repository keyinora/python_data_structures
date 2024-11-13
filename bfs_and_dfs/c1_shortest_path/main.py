class Graph:
    def bfs_path(self, start, end):
        # Check if the start or end vertex is not in the graph
        if start not in self.graph or end not in self.graph:
            return None

        # Initialize a queue for BFS, starting with the start vertex and an empty path
        queue = [(start, [start])]
        
        # Perform BFS until the queue is empty
        while queue:
            (current_vertex, path) = queue.pop(0)

            # Iterate over all neighbors of the current vertex
            for neighbor in self.graph[current_vertex]:
                if neighbor == end:
                    # Return the path if we reach the end vertex
                    return path + [end]
                elif neighbor not in path:
                    # Append the neighbor to the queue with the updated path
                    queue.append((neighbor, path + [neighbor]))

        # If no path is found, return None
        return None

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

