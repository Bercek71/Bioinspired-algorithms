import numpy as np
import plotly.graph_objects as go

class City:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def distance(self, other):
        return np.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def __eq__(self, other):
        return self.name == other.name and self.x == other.x and self.y == other.y

    def __copy__(self):
        return City(self.name, self.x, self.y)

    def __str__(self):
        return f"{self.name} ({self.x}, {self.y})"


class TravellingSalesmanProblem:
    def __init__(self, num_cities, max_x = 200, max_y = 200):
        self.num_cities = num_cities
        self.cities = []
        self.routes = []
        for i in range(num_cities):
            rand_x = np.random.randint(0, max_x)
            rand_y = np.random.randint(0, max_y)
            city_name = f"City {i}"
            city = City(city_name, rand_x, rand_y)
            self.cities.append(city)

    def setRoutes(self, routes):
        if len(routes) != self.num_cities + 1:
            raise ValueError("Route is not valid")
        self.routes = routes


    def show(self):
        x = [city.x for city in self.cities]
        y = [city.y for city in self.cities]
        #show cities as well as routes in plotly
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x, y=y, mode='markers+text', marker=dict(size=10), text=[city.name for city in self.cities]))
        for city in self.routes:
            city1 = self.cities[city]
            city2 = self.cities[self.routes[(self.routes.index(city) + 1) % self.num_cities]]
            fig.add_trace(go.Scatter(x=[city1.x, city2.x], y=[city1.y, city2.y], mode='lines', line=dict(width=1)))
        fig.show()








