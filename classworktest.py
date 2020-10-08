from genes import *

space = VerticesSpace((10, 4, 2))
assert space.nVertices == 10 + 4 + 2
space = VerticesSpace((1, 2, 2), [[2], [1, 3], [4, 5]])

print('Test Done!')