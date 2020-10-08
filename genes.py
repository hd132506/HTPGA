class VerticesSpace:
    """ Parameter
    contactLevels: Triple that contains the number of vertices for each contact level
    vertices: List of 3 vectors
    """
    def __init__(self, contactLevels, vertices=None):
        self.nVertices = sum(contactLevels)
        self.contactLevels = contactLevels
        self.space = []
        if vertices is None:
            self.makeAdam()
        else:
            self.space = vertices
    
    def makeAdam(self):
        # Vertices that contact with nothing
        self.space.append([i for i in range(1, self.contactLevels[0]+1)])
        # Vertices that contact with another vertex
        self.space.append([i for i in range(self.contactLevels[0]+1, sum(self.contactLevels[:2])+1)])
        # Vertices that contact with 2 vertices
        self.space.append([i for i in range(sum(self.contactLevels[:2])+1, self.nVertices+1)])