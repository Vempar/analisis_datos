import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from dash import Dash, html, dcc, callback, Output, Input
import dash_ag_grid as dag
import plotly.express as px

dc= pd.read_excel("datasets/datos_aleatorios.xlsx")


print(dc.head())
print(dc["Ingresos diarios"].describe())
print(dc["pesos"].describe())
print(dc["Kilometros"].describe())