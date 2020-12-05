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
    # Assuming Adam is created, space that has reversed order
    def makeEve(self):
        for i in range(len(self.__contactLevels)):
            self.__space[i].reverse()

    def flatten(self):
        flat = []
        for vector in self.__space:
            flat += vector
        return flat

    # The number of whole vertices
    def getnVertices(self):
        return self.__nVertices

    def getcontactLevels(self):
        return self.__contactLevels

    def space(self):
        return self.__space

    # Given contact level and index
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

    def contactLevels(self):
        return self.__contactLevels

    def nVertices(self):
        return self.__nVertices

    # Verify if the elements form a permutation from 0 to nVertices.
    def verify(self):
        hasAlready = [False for _ in range(self.__nVertices+1)]
        for lv in self.__space:
            for elem in lv:
                if hasAlready[elem]:
                    return False
                hasAlready[elem] = True
        return True

    def __len__(self):
        return self.__length

"""
A class including 6 tuples, which can perform operations to control VerticesSpace.
Not used directly, only Tortoise class can create/access to this class(Would be contained in Tortoise)
"""
class Hexagon:
    def __init__(self, coordinate=(0, 0), pointerList=None):
        self.__coordinate = coordinate
        self.__vertices = pointerList
        if self.__vertices == None:
            self.__vertices = [(0, 0) for i in range(6)]

    # Location info of the Hexagon in Tortoise
    def coordinate(self):
        return self.__coordinate

    # Mapping info between each vertex of the Hexagon and VerticesSpace
    def getPositions(self):
        return self.__vertices
    
    def getPosition(self, idx):
        return self.__vertices[idx]

    def setPosition(self, idx, position):
        # For initializing Tortoise
        self.__vertices[idx] = position
    
    # Would be abandoned
    def setVertex(self, space, loc, value):
        pos = self.__vertices[loc]
        space.setElement(pos, value)


"""
Actual class that GA would directly instantiate and call its methods.
1. Builds initial Vertices Space.
2. Builds a matrix structure consisted of Hexagons then maps each other.
This helps getting some features or insights like average values, neighboring elements from VerticesSpace through Hexagon.
"""
class Tortoise:
    def __init__(self, length, spaceType=None):
        self.__hexList = [[Hexagon((i, j)) for j in range(length)] for i in range(length)]
        self.__length = length
        self.__space = VerticesSpace(length, spaceType)
        self.__buildHexes()

    def __buildHexes(self):
        space_ptr = [0, 0, 0]
        lv_of_idx = [0 for i in range(6)]
        
        # Hexagon indices 0, 1, 2
        for i, row in enumerate(self.__hexList):
            for j, hexagon in enumerate(row):
                # Deciding the level(in a context of VerticesSpace) of each vertex
                if i == 0: # First row of tortoise
                    lv_of_idx[:3] = [1, 0, 1]
                else: # Other rows
                    lv_of_idx[:3] = [2, 2, 2]
                    if j == self.__length-1: # Last column not located in the first row
                        lv_of_idx[1] = 1
                if j == 0: # First column located in every row
                    lv_of_idx[0] -= 1
                if j == self.__length-1: # Last column located in every row
                    lv_of_idx[2] = 0

                hexagon.setPosition(0, (lv_of_idx[0], space_ptr[lv_of_idx[0]]))
                space_ptr[lv_of_idx[0]] += 1

                hexagon.setPosition(1, (lv_of_idx[1], space_ptr[lv_of_idx[1]]))
                space_ptr[lv_of_idx[1]] += 1

                hexagon.setPosition(2, (lv_of_idx[2], space_ptr[lv_of_idx[2]]))
                if j == self.__length-1:
                    space_ptr[lv_of_idx[2]] += 1

        # Hexagon indices 3, 4, 5
        for i, row in enumerate(self.__hexList[::-1]):
            for j, hexagon in enumerate(row):
                if i == 0: # Last row whose vertices haven't mapped yet 
                    lv_of_idx[3:] = [1, 0, 1]
                    if j == 0: # First column of the last row
                        lv_of_idx[3] = 0
                    if j == self.__length-1:
                        lv_of_idx[5] = 0

                    hexagon.setPosition(3, (lv_of_idx[3], space_ptr[lv_of_idx[3]]))
                    space_ptr[lv_of_idx[3]] += 1

                    hexagon.setPosition(4, (lv_of_idx[4], space_ptr[lv_of_idx[4]]))
                    space_ptr[lv_of_idx[4]] += 1

                    hexagon.setPosition(5, (lv_of_idx[5], space_ptr[lv_of_idx[5]]))
                    if j == self.__length-1:
                        space_ptr[lv_of_idx[5]] += 1
                    
                else:
                    if j == 0:
                        hexagon.setPosition(3, (0, space_ptr[0]))
                        space_ptr[0] += 1
                    else:
                        hexagon.setPosition(3, row[j-1].getPosition(5))

                    below = self.__hexList[-i][j]
                    hexagon.setPosition(4, below.getPosition(0))
                    hexagon.setPosition(5, below.getPosition(1))

    # Sum of all values in a single hexagon
    def singleHexagonValueSum(self, hexagon):
        return sum(self.getHexagonValues(hexagon))

    # List of 6 values in a hexagon
    def getHexagonValues(self, hexagon):
        posList = hexagon.getPositions()
        values = []
        for lv, pos in posList:
            values.append(self.__space.getElement(lv, pos))
        return values

    # List of adjacent hexagon objects
    def adjHexagons(self, hexagon):
        adjList = []
        r, c = hexagon.coordinate()
        inBound = lambda r, c: (0 <= r) and (r < self.__length) and (0 <= c) and (c < self.__length)
        coordinates = [(r-1, c), (r-1, c+1), (r, c-1), (r, c+1), (r+1, c-1), (r+1, c)]
        for row, col in coordinates:
            if inBound(row, col):
                adjList.append(self.__hexList[row][col])
        return adjList

    # Sum/mean of all the values in tortoise 
    def verticesSum(self, mean=False):
        space = self.__space.space()
        ret = sum(space[0]) + sum(space[1])*2 + sum(space[2])*3
        return ret / (self.__length**2) if mean else ret

    # Variance of hexagons, which might be used for calculating fitness
    def variance(self):
        mu = self.verticesSum(mean=True)
        aggr = 0
        for r in self.__hexList:
            for hexagon in r:
                aggr += (self.singleHexagonValueSum(hexagon) - mu)**2
        return aggr / (self.__length)**2

    # Hexagon object given its row and column index
    def getHexagon(self, row, col):
        return self.__hexList[row][col]

    # List(matrix) of all hexagons
    def getHexagons(self):
        return self.__hexList

    def __len__(self):
        return self.__length
    