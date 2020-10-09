"""
A class that represents chromosome.
contactLevels: Triple that contains the number of vertices for each contact level
vertices: List of 3 vectors
nVertices: The number of whole vertices, sum(contactLevels)
"""
class VerticesSpace:
    def __init__(self, contactLevels, vertices=None):
        self.__nVertices = sum(contactLevels)
        self.__contactLevels = contactLevels
        self.__space = []
        if vertices is None:
            self.makeAdam()
        else:
            self.__space = vertices
    
    # Class for building initial space
    def makeAdam(self):
        # Vertices that contact with nothing
        self.__space.append([i for i in range(1, self.__contactLevels[0]+1)])
        self.__space.append([i for i in range(self.__contactLevels[0]+1, sum(self.__contactLevels[:2])+1)])
        self.__space.append([i for i in range(sum(self.__contactLevels[:2])+1, self.__nVertices+1)])

    # Getter
    def getnVertices(self):
        return self.__nVertices
    def getcontactLevels(self):
        return self.__contactLevels
    def getspace(self):
        return self.__space

"""
A class which consists of 6 tuples, which can perform operations to control VerticeSpace.
"""
class Hexagon:
    def __init__(self, pointerList):
        pass