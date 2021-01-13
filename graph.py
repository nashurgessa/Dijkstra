
from vertex import Vertex

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())
    
    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)  # Entities # id=node, adjacent={}, distance=inf, visited=False, previous=False
        
        # Create a dictionary entity for each vertex
        """
        vert_dict = {
            'A': id='A', adjacent={}, distance=inf, visited=False, previous=False,
            'B': id='B', adjacent={}, distance=inf, visited=False, previous=False,
        }
        """
        self.vert_dict[node] = new_vertex
        return new_vertex
    
    def get_vertex(self, n):
        # If want to check if the vertex already exist in the graph
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None
        
    # Add edge
    def add_edge(self, frm, to, distance=0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)
        
        self.vert_dict[frm].add_neighbor(self.vert_dict[to], distance)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], distance)
        
    def get_vertices(self):
        return self.vert_dict.keys()
    
    def set_previous(self, current):
        self.previous = current
    
    def get_previous(self, current):
        return self.previous