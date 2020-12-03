"""
A class that represents chromosome.
contactLevels: Triple that contains the number of vertices for each contact level
vertices: List of 3 vectors
nVertices: The number of whole vertices, sum(contactLevels)
"""
class VerticesSpace:
    def __init__(self, length, vertices=None):
        self.__length = length
        self.__nVertices = 2*length*(length + 2)
        self.__contactLevels = (2+4*length, 4*(length-1), 2*(length-1)**2)
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
            self.__space[0] = space[:self.__contactLevels[0]]
            self.__space[1] = space[self.__contactLevels[0]+1:self.__contactLevels[0]+self.__contactLevels[1]]
            self.__space[2] = space[-self.__contactLevels[2]:]

    def __len__(self):
        return self.__nVertices

"""
A class which consists of 6 tuples, which can perform operations to control VerticesSpace.
Not used directly, only Tortoise class can create/access to this class(Would be contained in Tortoise)
"""
class Hexagon:
    def __init__(self, pointerList=None):
        self.__vertices = pointerList
        if self.__vertices == None:
            self.__vertices = [(0, 0) for i in range(6)]
            
    def getVerticesValues(self, space, index=None):
        values = []
        for lv, pos in self.__vertices:
            values.append(space.getElement(lv, pos))
        return values

    def getPositions(self):
        return self.__vertices
    
    def getPosition(self, pos):
        return self.__vertices[pos]

    def setPosition(self, idx, position):
        # Only used for initializing Tortoise
        self.__vertices[idx] = position
    
    def setVertex(self, space, loc, value):
        pos = self.__vertices[loc]
        space.setElement(pos, value)

class Tortoise:
    def __init__(self, length):
        # For each Hexagon, it can have at most 6 adjacent hexagons
        # adjMat[i][*] = j iff hexagon i is adjacent to hexagon j
        self.__adjMat = [[] for i in range(length)] # Might not be used
        self.__hexList = [[Hexagon() for j in range(length)] for i in range(length)]
        self.__length = length
        self.__space = VerticesSpace(length)
        self.buildHexes()

    def buildHexes(self):
        space_ptr = [0, 0, 0]
        
        # Hexagon index 0, 1, 2
        for i, row in enumerate(self.__hexList):
            for j, hexagon in enumerate(row):
                if i == 0:
                    idx0_lv = 1
                    idx1_lv = 0
                    idx2_lv = 1
                else:
                    idx0_lv = 2
                    idx1_lv = 2
                    idx2_lv = 2
                    if j == self.__length-1:
                        idx1_lv = 1
                if j == 0:
                    idx0_lv -= 1
                if j == self.__length-1:
                    idx2_lv = 0

                hexagon.setPosition(0, (idx0_lv, space_ptr[idx0_lv]))
                space_ptr[idx0_lv] += 1

                hexagon.setPosition(1, (idx1_lv, space_ptr[idx1_lv]))
                space_ptr[idx1_lv] += 1

                hexagon.setPosition(2, (idx2_lv, space_ptr[idx2_lv]))
                if j == self.__length-1:
                    space_ptr[idx2_lv] += 1

    def getHexagons(self):
        return self.__hexList

    def __len__(self):
        return self.__length
    