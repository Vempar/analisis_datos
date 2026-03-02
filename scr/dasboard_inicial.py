import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from dash import Dash, html, dcc, callback, Output, Input
import dash_ag_grid as dag
import plotly.express as px

dc= pd.read_excel("scr/datasets/datos_aleatorios.xlsx")

app=Dash("primer dash")
app.layout = [
    html.Div(children='My First App with Data, Graph, and Controls'),
    html.Hr(),
    dcc.RadioItems(options=['pop', 'lifeExp', 'gdpPercap'], value='lifeExp', id='my-final-radio-item-example'),
    dag.AgGrid(
        rowData=dc.to_dict('records'),
        columnDefs=[{"field": i} for i in dc.columns]
    ),
    dcc.Graph(figure={}, id='my-final-graph-example')
]

@callback(
    Output(component_id='my-final-graph-example', component_property='figure'),
    Input(component_id='my-final-radio-item-example', component_property='value')
)
def update_graph(col_chosen):
    fig = px.histogram(df, x='continent', y=col_chosen, histfunc='avg')
    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)