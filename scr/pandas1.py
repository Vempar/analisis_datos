import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame(
    {
        "Nombre": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss Elizabeth",
        ],
        "edad": [22, 35, 58],
        "Sexo": ["Hombre", "Hombre", "Mujer"],
    }
)
print(df)

print(df["edad"].max())  # Obtener el valor máximo de la columna "edad"
print(df["edad"].min())  # Obtener el valor mínimo de la columna "edad"
print(df["edad"].mean())  # Obtener el valor promedio de la columna "edad"
print(df.describe())  # Obtener estadísticas descriptivas de la columna "edad"


dc= pd.read_excel("./noviembre.xls", 
                    sheet_name="simplificada") # Cargar la hoja "dc" del archivo Excel

print(dc.head)# Mostrar las primeras filas del DataFrame cargado desde el archivo Excel
print(dc.describe())  # Obtener estadísticas descriptivas de las columnas numéricas del DataFrame
print(dc.dtypes) # Mostrar los tipos de datos de cada columna del DataFrame
print(dc) # Mostrar las primeras filas del DataFrame cargado desde la hoja "simplificada"
print(type(dc["total"])) # Mostrar el tipo de objeto del DataFrame cargado desde la hoja "simplificada"
print(dc["total"]) # Mostrar la columna "total" del DataFrame cargado desde la hoja "simplificada"
print(dc["total"].max())  # Obtener el valor máximo de la columna "total"
print(dc[dc["total"] < 20])  # Obtener las filas donde el valor de la columna "total" es menor a 20
print(dc["total"] < 20)  # Obtener una serie booleana indicando si el valor de la columna "total" es menor a 20
print(dc[dc["total"].isin([60])])  # Obtener las filas donde el valor de la columna "total" es 60
print(dc[dc["pago"].notna()])  # Obtener las filas donde el valor de la columna "pago" no es nulo
print(dc[(dc["pago"].notna()) & (dc["total"] > 250)])  # Obtener las filas donde el valor de la columna "pago" noes nulo y el valor de la columna "total" es mayor a 250
print(dc[dc["pago"].isna() & (dc["id"] == 1)])  # Obtener las filas donde el valor de la columna "pago" es nulo y el valor de la columna "id" es 1
print(dc.iloc[0])  # Obtener la primera fila del DataFrame utilizando iloc
print(dc.iloc[0:3])  # Obtener las primeras tres filas del DataFrame utilizando iloc
print(dc.loc[0])  # Obtener la primera fila del DataFrame utilizando loc    
print(dc.loc[0:3])  # Obtener las primeras tres filas del DataFrame utilizando loc
print(dc.loc[dc["total"] > 100, "pago"])  # Obtener los valores de la columna "pago" para las filas donde el valor de la columna "total" es mayor a 100 utilizando loc
print(dc.loc[dc["total"] > 100, ["pago", "total"]])  # Obtener los valores de las columnas "pago" y "total" para las filas donde el valor de la columna "total" es mayor a 100 utilizando loc
print(dc.iloc[2:3, 0:2])  # Obtener las filas 2 a 3 y las columnas 0 a 2 del DataFrame utilizando iloc
print(dc.loc[2:3, "id":"total"])  # Obtener las filas 2 a 3 y las columnas desde "id" hasta "total" del DataFrame utilizando loc
print(dc.sort_values("total", ascending=False))  # Ordenar el DataFrame por la columna "total" en orden descendente
print(dc.sort_values(["total", "pago"], ascending=[False, True]))  # Ordenar el DataFrame por las columnas "total" en orden descendente y "pago" en orden ascendente
plt.hist(dc["total"], bins=10)  # Crear un histograma de la columna "total" con 10 bins
plt.xlabel("Total")  # Etiqueta del eje x
plt.show()  # Mostrar el histograma
print(dc.shape) # Mostrar la forma del DataFrame (número de filas y columnas)
dc["nuevo total"]=dc["total"] * 1000 # Crear una nueva columna "nuevo total" que sea el producto de la columna "total" por 1000
print(dc.head())
dc_renamed=dc.rename(columns={"total": "total renombrado"})#Renombrar la columna "total" por "total renombrado"
print(dc_renamed.head())
de_renamed= dc.rename(columns=str.lower)#Renombrar todas las columnas a minusculas
print(dc_renamed.head())
print (dc["total"].mean())#Calcular el valor promedio de la columna "total"
print (dc["total"].median())#Calcular el valor mediano de la columna "total"
print (dc["total"].mode())#Calcular el valor modal de la columna "total"
print (dc["total"].std())#Calcular la desviación estándar de la columna "total"
print (dc["total"].var())#Calcular la varianza de la columna "total"
print (dc["total"].skew())#Calcular la curtosis de la columna "total"
print (dc["total"].kurt())#Calcular la curtosis de la columna "total"
print (dc["total"].quantile(0.25))#Calcular el cuantil 25% de la columna "total"
print (dc["total"].quantile(0.5))#Calcular el cuantil 50% de la columna "total"
print (dc["total"].quantile(0.75))#Calcular el cuantil 75% de la columna "total"
print (dc["total"].quantile(1))#Calcular el cuantil 100% de la columna "total"
dc_grop=dc.groupby("total").tail() #Obtener las últimas filas del DataFrame agrupado por la columna "total"
print(dc_grop)
dc_grop=dc[["id","total"]].groupby("total").mean#Obtener el valor promedio de la columna "total" agrupado por la columna "id"
print(dc_grop)
dc_grop=dc["id"].value_counts()#Obtener el valor de la columna "id" agrupado por la columna "total"
print(dc_grop)
dc_grop=dc["id"].count()#Obtener el valor de la columna "id" agrupado por la columna "total"
print(dc_grop)
dc_grap= dc.sort_values("pago", ascending=False)#Ordenar el DataFrame por la columna "pago" en orden descendente
print(dc_grap)
dc_grap=dc.sort_values(["total", "pago"], ascending=[False, True])#Ordenar el DataFrame por las columnas "total" en orden descendente y "pago" en orden ascendente
print(dc_grap)

dc_grap=dc.pivot_table(index="total", columns="pago", aggfunc="head") #Pivotar el DataFrame por las columnas "total" y "pago"
print(dc_grap)

dc_grap=dc.pivot(columns="pago", values="id").reset_index() #borramos el index
print(dc_grap)

dc_grap=dc.melt(id_vars=["id", "total"], value_vars=["pago"], value_name="prueba", var_name="prueba2") #trasforma la coluna y los encabezados
print(dc_grap)




