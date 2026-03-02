import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dc= pd.read_excel("./scr/datasets/datos_aleatorios.xlsx")
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
#imprime el numero de averias expresado en cifra por recorrido
print(dc.groupby("Recorrido")["Averia"].value_counts())
#imprime el numero de averias expresado en porcentaje por recorrido
print(dc.groupby("Recorrido")["Averia"].value_counts(normalize=True))

#crea una variable que almacene los datos de los recorridos que tengan averia y divuelva el porcentaje de averias por recorrido
recorrido_averia=dc[dc["Averia"]=="si"]
print(recorrido_averia.groupby("Recorrido")["Averia"].value_counts(normalize=True))

frecuencias= (dc["Averia"]=="si").sum()
print(frecuencias)


union=dc[dc["Recorrido"].isin(dc["Recorrido"].isin(["17/53"])) & (dc["Averia"]=="si")]
print(union)

col_union= dc[["Recorrido", "Averia"]]
print(col_union)

recorrido_selector= col_union["Recorrido"].isin(["17/53"])
print(recorrido_selector.sum())
print(recorrido_selector.value_counts())
print(recorrido_selector)  

Final = ((dc["Recorrido"] == "17/53") & (dc["Averia"] == "si")).sum()
print(Final)
Final = ((dc["Recorrido"] == "17/53") & (dc["Averia"] == "si")).value_counts()
print(Final)

print (((dc["Recorrido"] == "17/53") & (dc["Averia"] == "si")).sum())