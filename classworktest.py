from genes import *
from algorithm_skeleton import *

"""
This code performs tests defining requirements that each method must achieve, 
"""

def assertEqual(entity, target):
    try:
        assert entity == target
    except:
        print(f'{entity} is different from{target}')
        raise AssertionError

def VerticesSpaceTest():
    ## Space construction test
    space = VerticesSpace(2)
    assertEqual(space.getnVertices(), 16)
    assert space.verify()
    print('Space has been successfully constructed.')

    ## Set element test
    space = VerticesSpace(2)
    assertEqual(space.space(), [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14], [15, 16]])
    space.setElement((1, 1), 2)
    space.setElement((0, 0), 3)
    assertEqual(space.space(), [[3, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 2, 13, 14], [15, 16]])
    print('Element of a space can be set.')
    
    ## Set space test
    space = VerticesSpace(2)
    space.setSpace([[2, 1, 3, 4, 5, 6, 7, 8, 9, 10], [11, 2, 13, 14], [16, 15]])
    assertEqual(space.space(), [[2, 1, 3, 4, 5, 6, 7, 8, 9, 10], [11, 2, 13, 14], [16, 15]])
    print('A space can be set by also a list.')
    
    ## Flatten test
    assertEqual(space.flatten(), [2, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 2, 13, 14, 16, 15])


    ## Swap test
    space.swapElement((0,1), (0, 2))
    assertEqual(space.space(), [[2, 3, 1, 4, 5, 6, 7, 8, 9, 10], [11, 2, 13, 14], [16, 15]])
    assert space.verify() == False
    print('A space can be swapped.')

    ## Transformation test
    assertEqual(space.transformCoord(10), (1, 0))
    assertEqual(space.transformCoord(9), (0, 9))
    assertEqual(space.transformCoord(15), (2, 1))

def HexagonTest():
    pos = [(0, 0), (1, 0), (1, 1), (0, 6), (0, 4), (0, 2)]
    hex = Hexagon(pointerList=pos)
    hex.setPosition(2, (1, 2))
    assertEqual(hex.getPosition(2), (1, 2))
    print('Hexagon class has been successfully created.')

def TortoiseTest():
    t = Tortoise(length=3)
    assertEqual(len(t), 3)
    hl = t.getHexagons()
    for r in hl:
        for c in r:
            print(c.getPositions())
    assertEqual(list(map(Hexagon.coordinate, t.adjHexagons(t.getHexagon(0, 0)))), [(0, 1), (1, 0)])
    h = t.getHexagon(1, 2)
    assertEqual(t.getHexagonValues(h), [26, 18, 6, 29, 30, 20])
    assertEqual(t.singleHexagonValueSum(h), sum([26, 18, 6, 29, 30, 20]))
    print('mean:', t.verticesSum(mean=True))
    print('Tortoise class has been successfully created.')

def GATest():
    p = GeneticAlgorithm(length=2, population=10)


VerticesSpaceTest()
HexagonTest()
TortoiseTest()
GATest()
print('All Tests Done!')