import random

class AntColony:
    def __init__(self):
        self.ants = []
        self.best_path = []
        self.best_path_cost = float('inf')
        self.best_path_generation = 0
        self.history = []
        self.pheromones = []
        self.inverse_distances = []

    def initialize_pheromones_and_distances(self, tsp):
        num_cities = len(tsp.cities)
        self.pheromones = [[1 for _ in range(num_cities)] for _ in range(num_cities)]
        self.inverse_distances = [
            [1 / tsp.cities[i].distance(tsp.cities[j]) if i != j else 0 for j in range(num_cities)]
            for i in range(num_cities)
        ]


    def solve(self, tsp, num_ants, num_generations):
        self.history = []
        self.initialize_pheromones_and_distances(tsp)
        self.ants = [Ant(tsp, self.pheromones, self.inverse_distances) for _ in range(num_ants)]

        for generation in range(num_generations):
            for ant in self.ants:
                ant.find_path()
                if ant.path_cost < self.best_path_cost:
                    self.best_path = ant.path
                    self.best_path_cost = ant.path_cost
                    self.best_path_generation = generation
                    self.history.append(self.best_path)

            self.update_pheromones()
        return self.best_path, self.best_path_cost

    def update_pheromones(self):
        evaporation_rate = 0.5

        # Evaporate pheromones
        for i in range(len(self.pheromones)):
            for j in range(len(self.pheromones)):
                self.pheromones[i][j] *= evaporation_rate

        # Add new pheromone deposits
        for ant in self.ants:
            for i in range(len(ant.path) - 1):
                city1 = ant.path[i]
                city2 = ant.path[i + 1]
                self.pheromones[city1][city2] += 1 / ant.path_cost
                self.pheromones[city2][city1] += 1 / ant.path_cost


class Ant:
    def __init__(self, tsp, pheromones, inverse_distances):
        self.path = []
        self.path_cost = float('inf')
        self.tsp = tsp
        self.pheromones = pheromones
        self.inverse_distances = inverse_distances

    def find_path(self):
        self.path = []
        self.path_cost = 0
        num_cities = len(self.tsp.cities)

        # Start from a random city
        current_city = random.choice(range(num_cities))
        self.path.append(current_city)

        # Visit all cities
        while len(self.path) < num_cities:
            next_city = self.choose_next_city(current_city)
            self.path.append(next_city)
            self.path_cost += self.calculate_distance(current_city, next_city)
            current_city = next_city

        # Return to the starting city
        self.path.append(self.path[0])
        self.path_cost += self.calculate_distance(self.path[-2], self.path[0])

    def choose_next_city(self, current_city):
        alpha = 1  # Parameter to control influence of pheromone
        beta = 2   # Parameter to control influence of distance
        probabilities = []

        for city in range(len(self.tsp.cities)):
            if city not in self.path:  # Only consider unvisited cities
                tau = self.pheromones[current_city][city]
                eta = self.inverse_distances[current_city][city]
                probabilities.append((city, tau**alpha * eta**beta))

        total = sum(prob for _, prob in probabilities)

        if total == 0:
            # Handle the case where all probabilities are zero
            return random.choice([city for city in range(len(self.tsp.cities)) if city not in self.path])

        # Normalize probabilities
        probabilities = [(city, prob / total) for city, prob in probabilities]

        # Choose the next city based on probabilities
        next_city = random.choices(
            population=[city for city, _ in probabilities],
            weights=[prob for _, prob in probabilities],
            k=1
        )[0]
        return next_city

    def calculate_distance(self, city1, city2):
        return self.tsp.cities[city1].distance(self.tsp.cities[city2])