import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from dash import Dash, html, dcc, callback, Output, Input
import dash_ag_grid as dag
import plotly.express as px

dc= pd.read_excel("./scr/datasets/datos_aleatorios.xlsx")
recorrido_selector= "17/53"
#crea un grafico para ver la relacion entre el peso y los ingresos diarios
plt.bar(dc["Recorrido"]==recorrido_selector, dc["Averia"].count())
plt.xlabel("Recorrido")
plt.ylabel("Averia")
plt.title("Relacion entre recorrido y averia")
plt.show()

recorrido_averia = dc[dc["Averia"] == "si"]
counts = recorrido_averia["Recorrido"].value_counts()
plt.scatter(counts.index, counts.values, color=plt.cm.tab10(np.arange(len(counts))))
plt.xlabel("Recorrido")
plt.ylabel("Averia")
plt.title("Suma del numero de averias por recorrido")
plt.show()

plt.plot(counts.index, recorrido_averia["Recorrido"].value_counts())
plt.xlabel("Recorrido")
plt.ylabel("Averia")
plt.title("Suma del numero de averias por recorrido")
plt.show()

plt.scatter((dc["Recorrido"] == "17/53") & (dc["Averia"] == "si").sum(), (dc["Recorrido"] == "17/53"))
plt.xlabel("Recorrido")
plt.ylabel("Averia")
plt.title("Suma del numero de averias por recorrido")
plt.show()