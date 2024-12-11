import numpy as np

class FireflyAlgorithm:
    def __init__(self, population_size, function, m_max, t, dimension=2, alpha=0.5, beta_0=1.0, gamma=1.0):
        self.population_size = population_size
        self.function = function
        self.m_max = m_max
        self.dimension = dimension
        self.t = t
        self.alpha = alpha  # Randomness parameter
        self.beta_0 = beta_0  # Initial attractiveness
        self.gamma = gamma  # Absorption coefficient
        self.population = np.random.uniform(
            self.function.lower_bound, self.function.upper_bound, (population_size, self.dimension)
        )
        self.best_position = None
        self.best_fitness = float('inf')
        self.history = []

    def move_fireflies(self, i, j):
        r = np.linalg.norm(self.population[i] - self.population[j])
        # Přitažlivost
        beta = self.beta_0 * np.exp(-self.gamma * r**2)
        # Pohyb světlušky
        self.population[i] += beta * (self.population[j] - self.population[i]) + \
                              self.alpha * (np.random.rand(self.dimension) - 0.5)
        # Omezení hodnot na povolený rozsah
        self.population[i] = np.clip(self.population[i], self.function.lower_bound, self.function.upper_bound)

    def evaluate_population(self):
        # Výpočet fitness hodnot pro všechny jedince v populaci
        fitness_values = np.array([self.function.evaluate(ind) for ind in self.population])
        return fitness_values

    def search_min(self):
        for gen in range(self.m_max):
            fitness_values = self.evaluate_population()
            # Aktualizace nejlepší pozice
            best_index = np.argmin(fitness_values)
            if fitness_values[best_index] < self.best_fitness:
                self.best_fitness = fitness_values[best_index]
                self.best_position = self.population[best_index].copy()
                self.history.append((self.population[best_index].copy(), self.best_fitness))
            for i in range(self.population_size):
                for j in range(self.population_size):
                    if i == j: continue
                    if fitness_values[j] < fitness_values[i]:
                        self.move_fireflies(i, j)
        return self.best_position, self.best_fitness