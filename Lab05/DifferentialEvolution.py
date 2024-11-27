from copy import deepcopy
import numpy as np

class DifferentialEvolution:
    def __init__(self, number_of_individuals, generation_cycles, mutation_constant=0.5, crossover_range=0.5, dimension=2):
        self.number_of_individuals = number_of_individuals
        self.generation_cycles = generation_cycles
        self.mutation_constant = mutation_constant
        self.crossover_range = crossover_range
        self.dimension = dimension
        self.history = []

    def _initialize_population(self, function):
        return np.random.uniform(function.lower_bound, function.upper_bound, (self.number_of_individuals, self.dimension))

    def search(self, function):
        self.history = []
        self.function = function
        population = self._initialize_population(function)
        population_fitness = np.array([function.evaluate(individual) for individual in population])
        generation_count = 0

        while generation_count < self.generation_cycles:
            for i in range(self.number_of_individuals):
                while True:
                    a, b, c = np.random.choice(self.number_of_individuals, 3, replace=False)
                    if a != b and b != c and a != c:
                        break
            mutation_vector = population[a] + self.mutation_constant * (population[b] - population[c])
            trial_vector = np.zeros(self.dimension)
            j_rnd = np.random.randint(self.dimension)

            for j in range(self.dimension):
                if np.random.uniform(0, 1) < self.crossover_range or j == j_rnd:
                    trial_vector[j] = mutation_vector[j]
                else:
                    trial_vector[j] = population[i][j]

            evaluated_trial_vector = function.evaluate(trial_vector)

            if evaluated_trial_vector < population_fitness[i]:
                population[i] = trial_vector
                population_fitness[i] = evaluated_trial_vector
                self.history.append((deepcopy(population[i]), deepcopy(population_fitness[i])))

            generation_count += 1



        best_index = np.argmin(population_fitness)
        return population[best_index], population_fitness[best_index]

