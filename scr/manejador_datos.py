import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from dash import Dash, html, dcc, callback, Output, Input
import dash_ag_grid as dag
import plotly.express as px

dc= pd.read_excel("../scr/datasets/datos_aleatorios.xlsx")
peso_promedio=dc["pesos"]>8000
recorrido_selector= "17/53"
print(dc.head())
print(dc["Ingresos diarios"].describe())
print(dc["pesos"].describe())
print(dc["Kilometros"].describe())
#imprime los datos que tengan porte de primer porte y que los ingresos diarios sean mayores a 5000
print(dc[(dc["pesos"]>peso_promedio) & (dc["Ingresos diarios"]>5000)])
#imprime los datos que tengan porte de primer porte y que los ingresos diarios sean mayores a 5000 y que los kilometros sean mayores a 100
print(dc[(dc["pesos"]>peso_promedio) & (dc["Ingresos diarios"]>5000) & (dc["Kilometros"]>100)])
#imprime los datos que tengan porte de primer porte y que los ingresos diarios sean mayores a 5000 y que los kilometros sean mayores a 100 y que la averia sea si
print(dc[(dc["pesos"]>peso_promedio) & (dc["Ingresos diarios"]>5000) & (dc["Kilometros"]>100) & (dc["Averia"]=="si")])
#imprime solo las columnas peso y ingresos diarios
print(dc[["Recorrido","pesos", "Ingresos diarios"]])
#imprime solo las columnas peso y ingresos diarios que sean mayores a 5000

#imprime solo las columnas peso y ingresos diarios que sean mayores a 5000 y que los kilometros sean mayores a 100
print(dc[["Recorrido","pesos", "Ingresos diarios"]][(dc["pesos"]>peso_promedio) & (dc["Ingresos diarios"]>5000) & (dc["Kilometros"]>100)])
#imprime solo las columnas peso y ingresos diarios que sean mayores a 5000 y que los kilometros sean mayores a 100 y que la averia sea si
print(dc[["Recorrido","pesos", "Ingresos diarios"]][(dc["pesos"]>peso_promedio) & (dc["Ingresos diarios"]>5000) & (dc["Kilometros"]>100) & (dc["Averia"]=="si")])    

def filtrar_datos_recorrido(dc, peso_promedio, recorrido_selector):
    return dc[dc["Recorrido"]==recorrido_selector]

print(filtrar_datos_recorrido(dc, peso_promedio, recorrido_selector))

#crea un grafico para ver la relacion entre el peso y los ingresos diarios
plt.bar(dc["Recorrido"]==recorrido_selector, dc["Averia"].isin(["si"]))
plt.xlabel("Recorrido")
plt.ylabel("Averia")
plt.title("Relacion entre recorrido y averia")
plt.show()


#imprime el numero de averias expresado en cifra por recorrido
print(dc.groupby("Recorrido")["Averia"].value_counts())
#imprime el numero de averias expresado en porcentaje por recorrido
print(dc.groupby("Recorrido")["Averia"].value_counts(normalize=True))

#crea una variable que almacene los datos de los recorridos que tengan averia y divuelva el porcentaje de averias por recorrido
recorrido_averia=dc[dc["Averia"]=="si"]
print(recorrido_averia.groupby("Recorrido")["Averia"].value_counts(normalize=True))

#crea un grafico que muestre la suma del numero de averias por recorrido 17/53 y que tenga un color diferente para cada recorrido
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