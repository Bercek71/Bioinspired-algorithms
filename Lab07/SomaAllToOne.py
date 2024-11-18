import numpy as np
import random


class SomaAllToOne:
    def __init__(self, population_size, function, PRT, path_length, step, m_max, dimension=2):
        self.population_size = population_size
        self.function = function
        self.PRT = PRT
        self.path_length = path_length
        self.step = step
        self.m_max = m_max

        self.dimension = dimension
        self.population = np.random.uniform(self.function.lower_bound, self.function.upper_bound,
                                            (population_size, self.dimension))
        self.best_position = None
        self.best_fitness = float('inf')
        self.history = []

    def evaluate_population(self):
        fitness_values = np.array([self.function.evaluate(ind) for ind in self.population])
        return fitness_values

    def migrate(self):
        for i in range(self.population_size):
            individual = self.population[i]
            leader = self.best_position
            new_position = individual.copy()
            for t in np.arange(0, self.path_length, self.step):
                direction = (leader - individual) * (np.random.rand(self.dimension) < self.PRT)
                candidate_position = individual + t * direction

                candidate_position = np.clip(candidate_position, self.function.lower_bound, self.function.upper_bound)

                candidate_fitness = self.function.evaluate(candidate_position)

                if candidate_fitness < self.function.evaluate(new_position):
                    new_position = candidate_position

            self.population[i] = new_position

    def search_min(self):

        for gen in range(self.m_max):
            fitness_values = self.evaluate_population()

            min_idx = np.argmin(fitness_values)
            if fitness_values[min_idx] < self.best_fitness:
                self.best_fitness = fitness_values[min_idx]
                self.best_position = self.population[min_idx].copy()
                self.history.append((self.best_position, self.best_fitness))

            self.migrate()

        return self.best_position, self.best_fitness
