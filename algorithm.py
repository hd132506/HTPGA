from genes import *

class GeneticAlgorithm:
    def __init__(self, length, population):
        self.__length = length
        self.__population = population
        self.tortoise = [Tortoise(length) for _ in range(population)]
        # Additional parameters

    @staticmethod
    def fitness(tortoise):
        pass

    def mutate(self):
        pass

    def crossover(self):
        pass

    def select(self):
        pass

    def solve(self):
        pass