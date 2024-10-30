import numpy as np
from dash import Dash, html, dcc, Output, Input
from plotly import graph_objs as go

# funkce pro spuštění animace
def run_animation(history, cities):
    app = Dash(__name__)
    def create_initial_plot():
        #Create only cities in spate 200 x 200
        x = [city.x for city in cities]
        y = [city.y for city in cities]
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=x, y=y, mode='markers+text', marker=dict(size=10), text=[city.name for city in cities]))
        return fig


    initial_plot = create_initial_plot()

    app.layout = html.Div([
        html.Div([
            dcc.Graph(id='3d-surface', className="dash-graph2", style={"height": "100vh !important"}, ),
            html.Button('Start HillClimb Search', id='search-button'),
            dcc.Interval(id='interval-component', interval=100, n_intervals=0, disabled=True, max_intervals=len(history) - 1)
        ], style={"height": "100vh !important"})
    ])


    @app.callback(
        Output('interval-component', 'disabled'),
        Input('search-button', 'n_clicks')
    )
    def start_search(n_clicks):
        if n_clicks is None:
            return True
        if n_clicks > 0 and history is not None:
            return False  # Enable interval to start updates
        return True

    @app.callback(
        Output('3d-surface', 'figure'),
        Input('interval-component', 'n_intervals')
    )
    def update_graph(n_intervals):
        if n_intervals == 0:
            # with each interval add new route as line between cities
            fig = create_initial_plot()
            return fig
        else:
            # with each interval add new route as line between cities
            fig = create_initial_plot()
            # for i in range(n_intervals):
            x = [cities[city].x for city in history[n_intervals]]
            y = [cities[city].y for city in history[n_intervals]]
            fig.add_trace(go.Scatter
                                (x=x, y=y, mode='lines', line=dict(width=1)))
            return fig



    app.run_server(debug=True)
