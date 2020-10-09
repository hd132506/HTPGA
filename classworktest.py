from genes import *

def VerticesSpaceTest():
    space = VerticesSpace((10, 4, 2))
    assert space.getnVertices() == 10 + 4 + 2
    space = VerticesSpace((1, 2, 2), [[2], [1, 3], [4, 5]])
    # space.set

def HexagonTest():
    # pos = 
    # hex = Hexagon()
    # hex.setPos([()])
    # hex.rotate(space)
    pass

# p = Problem(n_hex=4)
# sol_space = p.solve()
print('Test Done!')