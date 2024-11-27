import random

class Ant:
    def __init__(self, tsp):
        self.path = []
        self.path_cost = float('inf')
        self.pheromones = []
        self.tsp = tsp
        for city in tsp.cities:
            self.pheromones.append([0] * len(tsp.cities))
            # city has   no id


    def find_path(self):
        # Initialize the path and path cost
        self.path = []
        self.path_cost = 0


        # Start from a random city
        current_city = random.choice(range(len(self.pheromones)))
        self.path.append(current_city)

        # Visit all cities
        while len(self.path) < len(self.pheromones):
            next_city = self.choose_next_city(current_city)
            self.path.append(next_city)
            self.path_cost += self.calculate_distance(current_city, next_city)
            current_city = next_city

        # Return to the starting city
        self.path_cost += self.calculate_distance(self.path[-1], self.path[0])

    def choose_next_city(self, current_city):
        probabilities = []
        for city in range(len(self.pheromones)):
            if city not in self.path:
                pheromone_level = self.pheromones[current_city][city]
                probabilities.append((city, pheromone_level))


        total_pheromone = sum(pheromone for city, pheromone in probabilities)
        if total_pheromone == 0:
            return random.choice([city for city in range(len(self.pheromones)) if city not in self.path])

        probabilities = [(city, pheromone / total_pheromone) for city, pheromone in probabilities]
        next_city = max(probabilities, key=lambda x: x[1])[0]
        return next_city


    def calculate_distance(self, city1, city2):
        return self.tsp.cities[city1].distance(self.tsp.cities[city2])

