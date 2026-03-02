import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from dash import Dash, html, dcc, callback, Output, Input
import dash_ag_grid as dag
import plotly.express as px

dc= pd.read_excel("scr/datasets/datos_aleatorios.xlsx")

app = Dash(__name__)

app.layout = html.Div([
    html.Div(children='Control Recorridos Pesos', style={'fontSize': '24px', 'fontWeight': 'bold', 'padding': '10px'}),
    dcc.Dropdown(
        id="mis_pesos",
        options=[{"label": r, "value": r} for r in dc["Recorrido"].unique()],
        value=dc["Recorrido"].unique()[0] if not dc.empty else None
    ),
    dcc.Graph(id="mis_pesos_salida"),
])

@callback(
    Output(component_id='mis_pesos_salida', component_property='figure'),
    Input(component_id='mis_pesos', component_property='value')
)
def update_graph(selected_recorrido):
    filtered_df = dc[dc["Recorrido"] == selected_recorrido]
    
    fig = px.line(
        filtered_df, 
        x="Fecha", 
        y="peso", 
        title=f"Pesos transportados en recorrido {selected_recorrido}",
        markers=True
    )
    
    fig.update_layout(
        xaxis_title="Fecha",
        yaxis_title="Kilos (peso)",
        template="plotly_white"
    )
    
    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)