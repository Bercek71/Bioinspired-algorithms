from Solution import Solution
from Functions import Function
import numpy as np
import random
import plotly.graph_objs as go


class BlindSearch(Solution):
    def __init__(self, function: Function, dimension=2, lower_bound=-5, upper_bound=5, iterations=100):
        super().__init__(function, dimension, lower_bound, upper_bound)
        self.iterations = iterations
        self.history = []
        self.best_solution = None
        self.best_value = None
    # Hledá minimum funkce
    def search_min(self):
        best_solution = None
        best_value = np.inf

        for _ in range(self.iterations):
            solution = [random.uniform(self.lower_bound, self.upper_bound) for _ in range(self.dimension)]
            value = self.function.evaluate(solution)
            self.history.append((solution, value))
            # Uložení nejlepšího řešení (liší se od maxima v podstatě jen znaménkem nerovnosti)
            if value < best_value:
                best_value = value
                best_solution = solution
        self.best_solution = best_solution
        self.best_value = best_value
        return best_solution, best_value
    # Vyhledá maximum
    def search_max(self):
        best_solution = None
        best_value = -np.inf

        for _ in range(self.iterations):
            solution = [random.uniform(self.lower_bound, self.upper_bound) for _ in range(self.dimension)]
            value = self.function.evaluate(solution)
            self.history.append((solution, value))

            if value > best_value:
                best_value = value
                best_solution = solution
        self.best_solution = best_solution
        self.best_value = best_value
        return best_solution, best_value

    # Vytvoření 3D grafu funkce a zvýraznění nejlepšího řešení
    def visualize_solution(self, best_solution=None, best_value=None):
        if best_solution is None or best_value is None:
            best_solution = self.best_solution
            best_value = self.best_value
        # Vytvoření prostoru pro vykreslení
        x = np.linspace(self.lower_bound, self.upper_bound, 100)
        y = np.linspace(self.lower_bound, self.upper_bound, 100)
        # Vytvoření mřížky
        X, Y = np.meshgrid(x, y)
        Z = np.array([[self.function.evaluate([i, j]) for i in x] for j in y])

        surface = go.Surface(z=Z, x=X, y=Y, colorscale='Viridis', opacity=0.7)
        scatter = go.Scatter3d(
            x=[best_solution[0]], y=[best_solution[1]], z=[best_value],
            mode='markers',
            marker=dict(size=5, color='red')
            )
        fig = go.Figure(data=[surface, scatter])
        fig.update_layout(
            title=f"Blind Search Visualization on {self.function.name}",
            scene=dict(xaxis_title="X", yaxis_title="Y", zaxis_title="Z")
        )



        fig.show()

