from enum import Enum
import numpy as np
import plotly.graph_objs as go
import plotly.io as pio

# pio.renderers.default = 'browser'

#Enum pro ruzne funkce
class FunctionType(Enum):
    SPHERE = 1
    ACKLEY = 2
    RASTRIGIN = 3
    ROSENBROCK = 4
    GRIEWANK = 5
    SCHWEFEL = 6
    LEVY = 7
    MICHALEWICZ = 8
    ZAKHAROV = 9

#Trida pro funkce
class Function:
    def __init__(self, functionType: FunctionType):
        self.name = functionType.name
        self.function = self._get_function(functionType)

    def _get_function(self, functionType):
        if functionType == FunctionType.SPHERE:
            return self._sphere
        elif functionType == FunctionType.ACKLEY:
            return self._ackley
        elif functionType == FunctionType.RASTRIGIN:
            return self._rastrigin
        elif functionType == FunctionType.ROSENBROCK:
            return self._rosenbrock
        elif functionType == FunctionType.GRIEWANK:
            return self._griewank
        elif functionType == FunctionType.SCHWEFEL:
            return self._schwefel
        elif functionType == FunctionType.LEVY:
            return self._levy
        elif functionType == FunctionType.MICHALEWICZ:
            return self._michalewicz
        elif functionType == FunctionType.ZAKHAROV:
            return self._zakharov

    # Vyhodnoceni funkce, x je pole hodno, na zaklade dimenze
    def evaluate(self, x):
        return self.function(x)

    # Vytvori 3D interaktivni graf
    def show_plot(self):
        x = np.linspace(-5, 5, 100)
        y = np.linspace(-5, 5, 100)
        X, Y = np.meshgrid(x, y)

        Z = np.array([[self.evaluate([i, j]) for i in x] for j in y])

        surface = go.Surface(z=Z, x=X, y=Y, colorscale='Viridis')

        layout = go.Layout(
            title=f"{self.name} Function 3D Plot",
            scene=dict(xaxis_title="X Axis", yaxis_title="Y Axis", zaxis_title="Z Axis")
        )

        fig = go.Figure(data=[surface], layout=layout)
        fig.show()

    def _sphere(self, x):
        return sum([i ** 2 for i in x])

    def _ackley(self, x):
        return -20 * np.exp(-0.2 * np.sqrt(sum([i ** 2 for i in x]) / len(x))) - \
               np.exp(sum([np.cos(2 * np.pi * i) for i in x]) / len(x)) + 20 + np.exp(1)

    def _rastrigin(self, x):
        return 10 * len(x) + sum([i ** 2 - 10 * np.cos(2 * np.pi * i) for i in x])

    def _rosenbrock(self, x):
        return sum([100 * (x[i + 1] - x[i] ** 2) ** 2 + (1 - x[i]) ** 2 for i in range(len(x) - 1)])

    def _griewank(self, x):
        return sum([i ** 2 / 4000 for i in x]) - np.prod([np.cos(i / np.sqrt(j + 1)) for j, i in enumerate(x)]) + 1

    def _schwefel(self, x):
        return 418.9829 * len(x) - sum([i * np.sin(np.sqrt(np.abs(i))) for i in x])

    def _levy(self, x):
        return np.sin(3 * np.pi * x[0]) ** 2 + \
               sum([(x[i] - 1) ** 2 * (1 + 10 * np.sin(np.pi * x[i] + 1) ** 2) for i in range(len(x) - 1)]) + \
               (x[-1] - 1) ** 2 * (1 + np.sin(2 * np.pi * x[-1]) ** 2)

    def _michalewicz(self, x):
        return -sum([np.sin(x[i]) * np.sin((i + 1) * x[i] ** 2 / np.pi) ** 20 for i in range(len(x))])

    def _zakharov(self, x):
        return sum([i ** 2 for i in x]) + \
               (sum([0.5 * i * (j + 1) for j, i in enumerate(x)]) ** 2) + \
               (sum([0.5 * i * (j + 1) for j, i in enumerate(x)]) ** 4)

