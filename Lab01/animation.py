import numpy as np
from dash import Dash, html, dcc, Output, Input
from plotly import graph_objs as go

# funkce pro spuštění animace
def run_animation(history, function):
    app = Dash(__name__)

    def create_initial_plot():
        x = np.linspace(-5, 5, 100)
        y = np.linspace(-5, 5, 100)
        X, Y = np.meshgrid(x, y)
        Z = np.array([[function.evaluate([i, j]) for i in x] for j in y])
        surface = go.Surface(z=Z, x=X, y=Y, colorscale='Viridis', opacity=0.7)
        return surface

    app.layout = html.B([
        dcc.Graph(id='3d-surface'),
        html.Button('Start Blind Search', id='search-button'),
        dcc.Interval(id='interval-component', interval=100, n_intervals=0, disabled=True, max_intervals=len(history))
    ])

    @app.callback(
        Output('interval-component', 'disabled'),
        Input('search-button', 'n_clicks')
    )
    def start_search(n_clicks):
        if n_clicks is None:
            return True
        if n_clicks > 0 and history:
            return False  # Enable interval to start updates
        return True

    @app.callback(
        Output('3d-surface', 'figure'),
        Input('interval-component', 'n_intervals')
    )
    def update_graph(n_intervals):
        if n_intervals == 0:
            # Vytvoří počáteční graf
            initial_surface = create_initial_plot()
            layout = go.Layout(title="Blind Search on Ackley Function",
                               scene=dict(xaxis_title="X", yaxis_title="Y", zaxis_title="Z"))
            return go.Figure(data=[initial_surface], layout=layout)

        else:
            values = []
            solutionsX = []
            solutionsY = []

            historyIndex = 0
            if n_intervals <= len(history):
                historyIndex = n_intervals
            else:
                historyIndex = len(history) - 1

            for i in range(historyIndex):
                solution, value = history[i]
                solutionsY.append(solution[1])
                solutionsX.append(solution[0])
                values.append(value)

            last_history_index = 0

            if n_intervals < len(history):
                last_history_index = n_intervals
            else:
                last_history_index = len(history) - 1

            solution, value = history[last_history_index]
            surface = create_initial_plot()

            # Postupně se prostupuje historií a zobrazují se jednotlivé body
            scatter_latest = go.Scatter3d(
                x=[solution[0]], y=[solution[1]], z=[value],
                mode='markers',
                marker=dict(size=5, color='blue')
            )
            scatter = go.Scatter3d(
                x=solutionsX, y=solutionsY, z=values,
                mode='markers',
                marker=dict(size=5, color='red')
            )

            layout = go.Layout(title="Blind Search on Ackley Function",
                               scene=dict(xaxis_title="X", yaxis_title="Y", zaxis_title="Z"))

            return go.Figure(data=[surface, scatter, scatter_latest], layout=layout)

        return go.Figure()

    app.run_server(debug=True)
