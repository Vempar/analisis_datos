import numpy as np
import pandas as pd
import os
from datetime import date, datetime
import random

filas = 1000
nombre=np.random.choice(["Juan", "Maria", "Pedro", "Ana", "Luis", "Marta", "Carlos", "Sofia", "Diego", "Laura"], size=filas)
apellido=np.random.choice(["Perez", "Gomez", "Garcia", "Rodriguez", "Fernandez", "Lopez", "Martinez", "Sanchez", "Perez", "Gomez"], size=filas)
nombre_completo=np.column_stack((nombre, apellido)).tolist()
Nomre_archivo="datos_aleatorios"
Complemento_archivo=np.random.randint(10000000, 99999999)
recorrido=np.random.choice(["17/53", "17/54", "17/55", "17/56", "17/57", "18/58", "18/59", "18/60", "18/61", "18/62", "11/63", "11/64", "11/65", "11/66", "11/67", "13/68", "13/69", "13/70", "13/71", "13/72", "13/73", "13/74", "13/75", "13/76", "13/77", "13/78", "13/79", "13/80", "13/81", "13/82", "13/83", "13/84", "13/85", "13/86", "13/87", "13/88", "13/89", "13/90", "13/91", "13/92", "13/93", "13/94", "13/95", "13/96", "13/97", "02/98", "02/99", "02/100"], size=filas)
porte= np.random.choice(["primer porte","segundo porte"],size=filas)
kilometro_recorridos=np.random.randint(10, 250, size=filas)
kilos_transportados=np.random.randint(10, 15000, size=filas)
combustible=np.random.randint(10, 100, size=filas)
fecha_inicio = date(2020, 1, 1)
fecha_fin = date(2025, 12, 31)
fecha_aleatoria2 = fecha_inicio + (fecha_fin - fecha_inicio) * random.random()

#genera fecha aleatoria para ponerlo en el dataframe con sus 1000 filas
fecha_aleatoria = pd.to_datetime(np.random.randint(1500000000, 1800000000, 1000), unit='s')





def crear_dataset():
    df=pd.DataFrame({
        "ID": np.arange(1, filas+1),
        "Fecha": fecha_aleatoria,
        "Recorrido": recorrido,
        "Porte": porte,
        "pesos": kilos_transportados,
        "Kilometros": kilometro_recorridos,
        "Combustible": combustible,
        "Conductor": nombre_completo,
        "Mozo1": nombre_completo,
        "Mozo2": nombre_completo,
        "Ingresos diarios": np.random.randint(2000, 10000, size=filas),
        "Averia": np.random.choice(["si", "no"], size=filas),
        
    })
    #crea un csv con los datos de df y lo guarde en el directorio datasets y si no exixte datasets lo crea
    if not os.path.exists("datasets"):
        os.makedirs("datasets")
    
    if os.path.exists("datasets/datos_aleatorios.json"):
        os.rename("datasets/datos_aleatorios.json", "datasets/datos_aleatorios_"+str(Complemento_archivo)+".json")
#crea el aarchivo en el directorio datasets y lo llama con la variable Nomre_archivo y el complemento archivo
    if os.path.exists("datasets/"+Nomre_archivo+".csv"):
        os.rename("datasets/"+Nomre_archivo+".csv", "datasets/"+Nomre_archivo+"_"+str(Complemento_archivo)+".csv")
    if os.path.exists("datasets/"+Nomre_archivo+".xlsx"):
        os.rename("datasets/"+Nomre_archivo+".xlsx", "datasets/"+Nomre_archivo+"_"+str(Complemento_archivo)+".xlsx")
    
    #crea un json con los datos de df y lo guarde en el directorio datasets y si no exixte datasets lo crea y si existe el archivo lo sobrescribe
    df.to_json("datasets/datos_aleatorios.json", index=False)
    #crea un csv con los datos de df y lo guarde en el directorio datasets y si no exixte datasets lo crea y si existe el archivo le cambia el nombre agregandole un numero al final
    df.to_csv("datasets/datos_aleatorios.csv", index=False)
    #crea un excel con los datos de df y lo guarde en el directorio datasets y si no exixte datasets lo crea y si existe el archivo le cambia el nombre agregandole una letra al final
    df.to_excel("datasets/datos_aleatorios.xlsx", index=False)
    #ejecuta la funcion crear_dataset
crear_dataset()


