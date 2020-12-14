from genes import *
from random import randint

class GeneticAlgorithm:
    def __init__(self, length, population):
        self.__length = length
        self.__population = population
        self.solutionSet = [Tortoise(length) for _ in range(population)]
        self.generation = 0
        # Additional parameters

    @staticmethod
    def fitness(tortoise):
        var = tortoise.variance()
        mean = tortoise.verticesSum(mean=True)
        return mean - (tortoise.nVertices()**.5) * (var**.5)


    def mutate(self, tortoise):
        nVertices = tortoise.getSpace().nVertices()
        pos1 = randint(0, nVertices)
        pos2 = randint(0, nVertices)
        tortoise.getSpace().swapElement(pos1, pos2)
        return tortoise

    def crossover(self, papa, mama):
        pa_vector = papa.getSpace().flatten()
        ma_vector = mama.getSpace().flatten()
        
        pass

    def select(self):
        pass

    def solve(self):
        pass