import sys
import numpy as np

class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        # Set initial distance to infinity
        self.distance = sys.maxsize # np.random.randint(10000, 100000, 1)#sys.maxsize
        # Set all nodes unvisited
        self.visited = False
        #  Predecessor
        self.previous = False
        
    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight
        
    def get_connections(self):
        return self.adjacent.keys()
    
    def get_id(self):
        return self.id
    
    def get_weight(self, neighbor):
        return self.adjacent[neighbor]
    
    def set_distance(self, dist):
        self.distance = dist
        
    def get_distance(self):
        return self.distance
    
    def set_previous(self, prev):
        self.previous = prev
    
    def set_visited(self):
        self.visited = True
        
    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])