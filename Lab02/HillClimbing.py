from operator import truediv

from Solution import Solution
import numpy as np

class HillClimbing(Solution):
    def __init__(self, function, dimension, points_per_cluster = 100, cluster_scale = 0.1):
        super().__init__(function, dimension, function.lower_bound, function.upper_bound)
        self.history = []
        self.points_per_cluster = points_per_cluster
        self.cluster_scale = cluster_scale
    def search(self, min = True):
        best_point = np.random.uniform(self.lower_bound, self.upper_bound, self.dimension)
        best_value = self.function.evaluate(best_point)

        while True:
            points = np.random.normal(best_point, self.cluster_scale, (self.points_per_cluster, self.dimension))
            points = np.clip(points, self.lower_bound, self.upper_bound)

            values = [self.function.evaluate(point) for point in points]
            best_point_value = None
            if min:
                best_point_value = np.min(values)
            else:
                best_point_value = np.max(values)


            best_point_in_cluster = None
            if min:
                best_point_in_cluster = points[np.argmin(values)]
            else:
                best_point_in_cluster = points[np.argmax(values)]

            if (best_point_value < best_value and min) or (best_point_value > best_value and not min):
                best_point = best_point_in_cluster
                best_value = best_point_value
                self.history.append((best_point, best_value))
            else:
                break
        return best_point


    def search_min(self):
        return self.search(min = True)

    def search_max(self):
        return self.search(min = False)