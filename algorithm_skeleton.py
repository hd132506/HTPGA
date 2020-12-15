from genes import *
from random import randint, sample, choices, random
from itertools import permutations

class GeneticAlgorithm:
    def __init__(self, length, population):
        self.length = length
        self.population = population
        self.solutionSet = [Tortoise(length) for _ in range(population)]
        self.bestSolution = [Tortoise(length), 0]
        # Eve
        for t in self.solutionSet[length:]:
            t.getSpace().makeEve()
        self.generation = 0
        # Additional parameters
        self.t = 0.90 # Tournament variable

    def fitness(self, tortoise):
        var = tortoise.variance()
        mean = tortoise.verticesSum(mean=True)
        fit = mean - (tortoise.nVertices()**.5) * (var**.5)

        if var == .0:
            fit += 1000

        if fit > self.bestSolution[1]:
            self.bestSolution[0].getSpace().setSpace(tortoise.getSpace().flatten())
            self.bestSolution[1] = fit
        return fit


    def mutate(self, tortoise):
        nVertices = tortoise.getSpace().nVertices()
        pos1 = randint(0, nVertices-1)
        pos2 = randint(0, nVertices-1)
        tortoise.getSpace().swapElement(pos1, pos2)
        return tortoise

    # Cycle
    def crossover(self, papa, mama):
        pa_vector = papa.getSpace().flatten()
        ma_vector = mama.getSpace().flatten()
        vector_size = len(pa_vector)
        origin = pa_vector
        toggle = lambda x: pa_vector if x == ma_vector else ma_vector

        child_vector = [0 for _ in range(vector_size)]
        left_idx = 0

        while left_idx < vector_size:
            ptr = left_idx
            while child_vector[ptr] == 0:
                child_vector[ptr] = origin[ptr]
                ptr = origin.index(toggle(origin)[ptr])

            while left_idx < vector_size and child_vector[left_idx] != 0:
                left_idx += 1
            origin = toggle(origin)

        if self.fitness(papa) > self.fitness(mama):
            mama.getSpace().setSpace(child_vector)
        else:
            papa.getSpace().setSpace(child_vector)

    def tournament(self, participants):
        length = len(participants)
        if length == 1:
            return (participants[0], self.fitness(participants[0]))
        left = self.tournament(participants[:length//2])
        right = self.tournament(participants[length//2:])
        if left[1] < right[1]:
            return right if random() < self.t else left
        else:
            return left if random() < self.t else right
            
    
    # Tournament
    def select(self):
        num = 8
        samples = sample(self.solutionSet, k=num)

        return self.tournament(samples)[0]

    def repair(self, tortoise, matured=False):
        nVertices = tortoise.getSpace().nVertices()
        intensity = choices(range(2, 6), weights = [2, 6, 3, 1], k=1)[0]
        
        space = tortoise.getSpace().flatten()

        target_indices = sample(range(nVertices), k=intensity)
        target_values = [space[i] for i in target_indices]

        comparison_tortoise = Tortoise(self.length)
        best_fitness = self.fitness(tortoise)
        for suggestion in permutations(target_values, intensity):
            for i, j in enumerate(target_indices):
                space[j] = suggestion[i]
            comparison_tortoise.getSpace().setSpace(space)
            
            if best_fitness < self.fitness(comparison_tortoise):
                # best_fitness = current_fitness
                tortoise.getSpace().setSpace(space)

        if matured and self.length > 2:
            cont_lv = tortoise.getSpace().contactLevels()
            target_indices = [sample(range(0, cont_lv[0]), k=3), 
                            sample(range(cont_lv[0], cont_lv[0]+cont_lv[1]), k=3),
                            sample(range(cont_lv[0]+cont_lv[1], nVertices), k=3)]
            target_values = [[space[i] for i in lv] for lv in target_indices]
            
            for lv0_suggest in permutations(target_values[0], 3):
                for i, j in enumerate(target_indices[0]):
                    space[j] = lv0_suggest[i]

                for lv1_suggest in permutations(target_values[1], 3):
                    for i, j in enumerate(target_indices[1]):
                        space[j] = lv1_suggest[i]
                    
                    for lv2_suggest in permutations(target_values[2], 3):
                        for i, j in enumerate(target_indices[2]):
                            space[j] = lv2_suggest[i]
                        comparison_tortoise.getSpace().setSpace(space)
                        current_fitness = self.fitness(comparison_tortoise)
                        if best_fitness < current_fitness:
                            best_fitness = current_fitness
                            tortoise.getSpace().setSpace(space)


    def avg_fitness(self):
        fitness_list = [self.fitness(t) for t in self.solutionSet]
        return sum(fitness_list) / self.population

    def var_fitness(self):
        fitness_list = [self.fitness(t) for t in self.solutionSet]
        mean = sum(fitness_list) / self.population

        sqrdev = lambda x: (x-mean)**2
        
        return sum([sqrdev(x) for x in fitness_list]) / self.population

    def solve(self):
        step = 2000
        for i in range(step):
            # Mutation
            for tortoise in self.solutionSet:
                if random() < (1 - i*(10/step)):
                    self.mutate(tortoise)


            # Crossover
            for _ in range(int(self.population*0.3)):
                self.crossover(self.select(), self.select())
            
            
            # Repair
            for tortoise in self.solutionSet:
                if random() < 0.7:
                    self.repair(tortoise)
                if 0.9*step < i and random() < 0.1:
                    self.repair(tortoise, matured=True)
            
            if i % 10 == 0:
                stddev = self.var_fitness()**(.5)
                print(f"Maximum fitness in step {i}: {self.bestSolution[1]}, Average: {self.avg_fitness()}, \
                Standard deviation: {stddev}")
                if stddev < 0.2:
                    break
        

p = GeneticAlgorithm(length=3, population=100)

p.solve()
print(p.bestSolution[1])
print(p.bestSolution[0].getSpace().space())
p.bestSolution[0].show()