from Solution import Solution
import numpy as np

class SimulatedAnnealing(Solution):
    def __init__(self, function, temperature = 100, cooling_rate = 0.8, minimal_temperature = 1, cluster_scale = 0.1):
        super().__init__(function, 2, function.lower_bound, function.upper_bound)
        self.temperature = temperature
        self.cooling_rate = cooling_rate
        self.cluster_scale = cluster_scale
        self.history = []
        self.minimal_temperature = minimal_temperature


    def search(self, min = True):
        self.history = []

        best_point = np.random.uniform(self.lower_bound, self.upper_bound, self.dimension)
        best_value = self.function.evaluate(best_point)
        # dokud neni teplota mensi nez minimalni
        while self.temperature > self.minimal_temperature:
            new_point = np.random.normal(best_point, self.cluster_scale, self.dimension)
            new_point = np.clip(new_point, self.lower_bound, self.upper_bound)
            new_value = self.function.evaluate(new_point)
            # pokud je nova hodnota lepsi nez ta nejlepsi, ji ulozim
            if (new_value < best_value and min) or (new_value >= best_value and not min):
                best_point = new_point
                best_value = new_value
                self.history.append((best_point, best_value))
            else:
                # pokud je nova hodnota horsi, tak ji ulozim s pravdepodobnosti
                if np.random.rand() < np.exp((best_value - new_value) / self.temperature):
                    best_point = new_point
                    best_value = new_value
                    self.history.append((best_point, best_value))
            self.temperature *= self.cooling_rate

        return best_point, best_value


    def search_min(self):
        return self.search(min = True)

    def search_max(self):
        return self.search(min = False)



