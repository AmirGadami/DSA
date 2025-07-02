class Graph:
    """
    An undirected graph implemented using an adjacency list.

    Attributes:
        adj_list (dict): A dictionary mapping vertices to lists of adjacent vertices.

    Methods:
        print_graph(): Prints all vertices and their adjacency lists.
        add_vertex(vertex): Adds a new vertex to the graph.
        add_edge(v1, v2): Adds an undirected edge between v1 and v2.
        remove_edge(v1, v2): Removes the edge between v1 and v2.
        remove_vertex(vertex): Removes a vertex and all its edges.
    """

    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        # Print each vertex and its connected vertices
        v_list = sorted(self.adj_list.keys())
        for v in v_list:
            print(v, ':', self.adj_list[v])

    def add_vertex(self, vertex):
        # Add a new vertex if it doesn't already exist
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2):
        # Add an undirected edge between v1 and v2
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self, v1, v2):
        # Remove the edge between v1 and v2
        if v1 in self.adj_list and v2 in self.adj_list: 
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:
                pass  # Edge doesn't exist
            return True
        return False

    def remove_vertex(self, vertex):
        # Remove a vertex and all connected edges
        if vertex in self.adj_list:
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False