class Graph:
    
    def __init__ (self, adj = None):
        ''' Creates new graph from adjacency list. '''
        
        if adj is None:
            adj = []
            
        self.adj = adj
        
    def GetEdges (self):
        ''' Returns list of the graph's edges. '''
        
        edges = []
        
        for vertex in self.adj:
            for edge in self.adj [vertex]:
                if {edge, vertex} not in edges:
                    edges.append ({vertex, edge})
                    
        return edges
    
    def AddEdge (self, edge):
        ''' Adds edge to adj. dict if not present. '''
        
        edge = set (edge)
        (vertexOne, vertexTwo) = tuple (edge)
        
        if vertexOne in self.adj:
            self.adj [vertexOne].append (vertexTwo)
        else:
            self.adj [vertexOne] = [vertexTwo]
                    
    def GetVertices (self):
        ''' Returns list of the graph's vertices. '''
        
        return list (self.adj.keys ())
    
    def AddVertex (self, vertex):
        ''' Adds vertex to adjacency dict as key. '''
        
        if vertex not in self.adj:
            self.adj [vertex] = []                   
    
