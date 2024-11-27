from Ant import Ant


class AntColony:
    def __init__(self):
        self.ants = []
        self.best_path = []
        self.best_path_cost = float('inf')
        self.best_path_generation = 0
        self.history = []


    def solve(self, tsp, num_ants, num_generations):
        self.history = []
        self.ants = [Ant(tsp) for _ in range(num_ants)]

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

        for city in range(len(self.best_path) - 1):
            for ant in self.ants:
                ant.pheromones[city][city + 1] += 1 / ant.path_cost

        for ant in self.ants:
            for city in range(len(ant.pheromones)):
                for neighbor in range(len(ant.pheromones[city])):
                    ant.pheromones[city][neighbor] *= evaporation_rate


