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

        if (vertices is None) or (vertices == 'Adam'):
            self.makeAdam()
        elif vertices == 'Eve':
            self.makeEve()
        else:
            self.__space = vertices
        
        
    
    # Class for building initial space 
    def makeAdam(self):
        # For each space seperated by contact level, fill with just simple sequential numbers
        # So that it can be an initial, seed chromosome(Adam)
        if self.__space == []:
            
            self.__space.append([i for i in range(1, self.__contactLevels[0]+1)])
            self.__space.append([i for i in range(self.__contactLevels[0]+1, sum(self.__contactLevels[:2])+1)])
            self.__space.append([i for i in range(sum(self.__contactLevels[:2])+1, self.__nVertices+1)])
    def makeEve(self):
        self.makeAdam()
        for i in range(len(self.__space)):
            self.__space[i].reverse()
    # Getter
    def getnVertices(self):
        return self.__nVertices
    def getcontactLevels(self):
        return self.__contactLevels
    def getspace(self):
        return self.__space

    # Setter / modifier
    def setElement(self, pos, value):
        self.__space[pos[0]][pos[1]] = value

"""
A class which consists of 6 tuples, which can perform operations to control VerticeSpace.
"""
class Hexagon:
    def __init__(self, pointerList):
        pass