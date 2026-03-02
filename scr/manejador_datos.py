import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from dash import Dash, html, dcc, callback, Output, Input
import dash_ag_grid as dag
import plotly.express as px

dc= pd.read_excel("scr/datasets/datos_aleatorios.xlsx")


print(dc.head())
print(dc["Ingresos diarios"].describe())
print(dc["pesos"].describe())
print(dc["Kilometros"].describe())
#imprime los datos que tengan porte de primer porte y que los ingresos diarios sean mayores a 5000
print(dc[(dc["pesos"]>5000) & (dc["Ingresos diarios"]>5000)])
#imprime los datos que tengan porte de primer porte y que los ingresos diarios sean mayores a 5000 y que los kilometros sean mayores a 100
print(dc[(dc["pesos"]>5000) & (dc["Ingresos diarios"]>5000) & (dc["Kilometros"]>100)])
#imprime los datos que tengan porte de primer porte y que los ingresos diarios sean mayores a 5000 y que los kilometros sean mayores a 100 y que la averia sea si
print(dc[(dc["pesos"]>5000) & (dc["Ingresos diarios"]>5000) & (dc["Kilometros"]>100) & (dc["Averia"]=="si")])
#imprime solo las columnas peso y ingresos diarios
print(dc[["pesos", "Ingresos diarios"]])
#imprime solo las columnas peso y ingresos diarios que sean mayores a 5000
print(dc[["pesos", "Ingresos diarios"]][dc["pesos"]>5000])
#imprime solo las columnas peso y ingresos diarios que sean mayores a 5000 y que los kilometros sean mayores a 100
print(dc[["pesos", "Ingresos diarios"]][(dc["pesos"]>5000) & (dc["Ingresos diarios"]>5000) & (dc["Kilometros"]>100)])
#imprime solo las columnas peso y ingresos diarios que sean mayores a 5000 y que los kilometros sean mayores a 100 y que la averia sea si
print(dc[["pesos", "Ingresos diarios"]][(dc["pesos"]>5000) & (dc["Ingresos diarios"]>5000) & (dc["Kilometros"]>100) & (dc["Averia"]=="si")])    