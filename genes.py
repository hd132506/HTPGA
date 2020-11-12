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
            self.makeAdam()
            self.makeEve()
        else:
            self.__space = vertices
        
        
    
    # Class for building initial space 
    def makeAdam(self):
        # For each space seperated by contact level, fill with just simple sequential numbers
        # So that it can be an initial, seed chromosome(Adam)
        base = 1
        if self.__space == []:
            for nlv in self.__contactLevels:
                self.__space.append([i for i in range(base, base+nlv)])
                base += nlv

    def makeEve(self):
        for i in range(len(self.__contactLevels)):
            self.__space[i].reverse()

    def flatten(self):
        flat = []
        for vector in self.__space:
            flat += vector
        return flat

    # Getter
    def getnVertices(self):
        return self.__nVertices
    def getcontactLevels(self):
        return self.__contactLevels
    def getspace(self):
        return self.__space
    def getElement(self, lv, pos):
        return self.__space[lv][pos]

    # Setter / modifier
    def setElement(self, pos, value):
        self.__space[pos[0]][pos[1]] = value

    def swapElement(self, pos1, pos2):
        tmp = self.__space[pos1[0]][pos1[1]]
        self.__space[pos1[0]][pos1[1]] = self.__space[pos2[0]][pos2[1]]
        self.__space[pos2[0]][pos2[1]] = tmp

    def setSpace(self, space):
        if type(space[0]) is list: # if space is given list of lists
            self.__space = space
        else: # if space is given flat list
            for i in range(len(self.__contactLevels)):
                self.__space[i] = space[:self.__contactLevels[i]]

"""
A class which consists of 6 tuples, which can perform operations to control VerticesSpace.
"""
class Hexagon:
    def __init__(self, pointerList):
        self.__vertices = pointerList
    def getVerticesValues(self, space, index=None):
        values = []
        for lv, pos in self.__vertices:
            values.append(space.getElement(lv, pos))
        return values

    def getPositions(self):
        return self.__vertices
    
    def setVertex(self, space, loc, value):
        pos = self.__vertices[loc]
        space.setElement(pos, value)

class Tortoise:
    def __init__(self, length):
        self.__adjMat = [[0 for j in range(length)] for i in range(length)]