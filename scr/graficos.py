import pandas as pd
import matplotlib.pyplot as plt


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

#grafica de lineas es buena para grancantidad de datos y tendencias. analisis de regresion y series de tiempo
plt.plot(counts.index, recorrido_averia["Recorrido"].value_counts())
plt.xlabel("Recorrido")
plt.ylabel("Averia")
plt.title("Suma del numero de averias por recorrido")
plt.show()

#grafica de dispersion es buena para ver la relacion entre dos variables
plt.scatter(dc["Recorrido"], dc["Averia"])
plt.xlabel("Recorrido")
plt.ylabel("Averia")
plt.title("Relacion entre recorrido y averia")
plt.show()

#grafica de barras buena para conteos agrupaciond e datos y facil de explicar
plt.bar(counts.index, recorrido_averia["Recorrido"].value_counts())
plt.xlabel("Recorrido")
plt.ylabel("Averia")
plt.title("Suma del numero de averias por recorrido")
plt.show()

#grafica de pastel buena para proporciones y porcentajes no es buena en 3d
plt.pie(recorrido_averia["Recorrido"].value_counts(), labels=recorrido_averia["Recorrido"].value_counts().index)
plt.title("Suma del numero de averias por recorrido")
plt.show()