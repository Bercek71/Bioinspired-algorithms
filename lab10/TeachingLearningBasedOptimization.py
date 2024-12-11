import numpy as np

class TeachingLearningBasedOptimization:
    def __init__(self, function, population_size: int, dimension: int, iterations: int):
        self.function = function
        self.population_size = population_size
        self.dimension = dimension
        self.iterations = iterations
        self.population = np.random.uniform(function.lower_bound, function.upper_bound, (population_size, dimension))
        self.best_solution = self.population[0]
        self.best_fitness = self.function.evaluate(self.best_solution)
        self.history = []

    def search_min(self):
        for i in range(self.iterations):
            for j in range(self.population_size):
                teacher = self.population[j]
                # vyber studenta
                student = self.population[np.random.randint(0, self.population_size)]
                # uceni
                if self.function.evaluate(teacher) < self.function.evaluate(student):
                    self.population[j] = np.clip(teacher + np.random.uniform(-1, 1) * (teacher - student), self.function.lower_bound, self.function.upper_bound)
                else:
                    self.population[j] = np.clip(teacher + np.random.uniform(-1, 1) * (student - teacher), self.function.lower_bound, self.function.upper_bound)
                # nahradit nejlepsiho jedince
                if self.function.evaluate(self.population[j]) < self.best_fitness:
                    self.best_solution = self.population[j].copy()
                    self.best_fitness = self.function.evaluate(self.population[j]).copy()
                    self.history.append((self.best_solution.copy(), self.best_fitness.copy()))
        return self.best_solution, self.best_fitness