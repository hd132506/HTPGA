from genes import *

def assertEqual(entity, target):
    try:
        assert entity == target
    except:
        print(f'{entity} is different from{target}')
        raise AssertionError

def VerticesSpaceTest():
    ## Space construction test
    space = VerticesSpace((5, 3, 2))
    assertEqual(space.getnVertices(), sum((5, 3, 2)))
    assertEqual(space.getspace(), [[1, 2, 3, 4, 5], [6, 7, 8], [9, 10]])
    space = VerticesSpace((5, 3, 2), 'Eve')
    assertEqual(space.getspace(), [list(reversed([1, 2, 3, 4, 5])), list(reversed([6, 7, 8])), list(reversed([9, 10]))])
    print('Space has been successfully constructed.')

    space = VerticesSpace((1, 2, 2), [[2], [1, 3], [4, 5]])
    ## Set element test
    space.setElement((1, 1), 2)
    space.setElement((0, 0), 1)
    assertEqual(space.getspace(), [[1], [1, 2], [4, 5]])

    print('Element of a space can be set.')

    ## Swap test
    # space.swapElement((0,1), (0, 2))
    # print(space.getspace())

def HexagonTest():
    # pos = 
    # hex = Hexagon()
    # hex.setPos([()])
    # hex.rotate(space)
    pass

# p = Problem(n_hex=4)
# sol_space = p.solve()


VerticesSpaceTest()
print('All Tests Done!')