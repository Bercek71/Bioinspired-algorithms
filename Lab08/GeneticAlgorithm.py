import numpy as np

class GeneticAlgorithm:
    def __init__(self, population_size, num_generations):
        self.population_size = population_size
        self.num_generations = num_generations
        self.history = []

    def _initialize_population(self, tsp):
        population = []
        for i in range(self.population_size):
            route = list(range(tsp.num_cities))
            np.random.shuffle(route)
            route.append(route[0])
            population.append(route)
        return population


    def _calculate_distance(self, route, tsp):
        distance = 0
        for i in range(len(route) - 1):
            distance += tsp.cities[route[i]].distance(tsp.cities[route[i + 1]])
        return distance

    def _evaluate_population(self, population, tsp):
        distances = []
        for route in population:
            distance = self._calculate_distance(route, tsp)
            distances.append(distance)
        return distances

    def _crossover(self, parent_a, parent_b):
        split = np.random.randint(1, len(parent_a) - 1)
        child = parent_a[:split]
        for i in range(1, len(parent_b)):
            if parent_b[i] not in child:
                child.append(parent_b[i])
        child.append(child[0])
        return child




    def mutate(self, offspring):
        idx1 = np.random.randint(1, len(offspring) - 1)
        idx2 = np.random.randint(1, len(offspring) - 1)
        offspring[idx1], offspring[idx2] = offspring[idx2], offspring[idx1]
        return offspring

    def solve(self, tsp):
        population = self._initialize_population(tsp)
        for i in range(self.num_generations):
            new_population = population.copy()
            fitness = self._evaluate_population(new_population, tsp)

            for j in range(self.population_size):
                parent_a = population[j]
                while True:
                    parent_b = population[np.random.randint(0, self.population_size)]
                    if parent_a != parent_b:
                        break

                child = self._crossover(parent_a, parent_b)
                if np.random.uniform() < 0.5:
                    child = self.mutate(child)

                if self._calculate_distance(child, tsp) < fitness[j]:
                    new_population[j] = child
            population = new_population
            popul_eval = self._evaluate_population(population, tsp)
            if population[np.argmin(popul_eval)] not in self.history:
                self.history.append(population[np.argmin(popul_eval)])


        return population[np.argmin(self._evaluate_population(population, tsp))], np.min(self._evaluate_population(population, tsp))
