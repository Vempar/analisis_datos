import numpy as np

Numeros_primos_lista= [2,3,5,7,11,13,17,19,23,29]

numeros_primos_array= np.array(Numeros_primos_lista)
Array_zeros= np.zeros(10)
Array_unos= np.ones(10)
Array_unos_enteros= np.ones(10, dtype=int)
Array_rango= np.arange(10)
#empieza en 0, termina en 10, avanza de 2 en 2
Array_rango_pasos= np.arange(0,10,2)
#empieza en 0, termina en 10, avanza de 0.5 en 0.5
Array_rango_decimales= np.arange(0,10,0.5)

#crea un array de 10 elementos entre 0 y 10
Array_linspace= np.linspace(0,10,10)

Array_aleatorio= np.random.rand(10)
Array_aleatorio_enteros= np.random.randint(0,10,10)

array_matriz= np.array([[1,2,3],[4,5,6],[7,8,9]])
array_reshape= array_matriz.reshape(3,3)

#suma de todos los elementos del array
array_reshape.sum()
#media de todos los elementos del array
array_reshape.mean()
#mediana de todos los elementos del array
array_reshape.median()
#moda de todos los elementos del array
array_reshape.mode()
#desviacion estandar de todos los elementos del array
array_reshape.std()
#varianza de todos los elementos del array
array_reshape.var()
#raiz cuadrada de todos los elementos del array
array_reshape.sqrt()
#potencia de todos los elementos del array
array_reshape.power()
#logaritmo de todos los elementos del array
array_reshape.log()
#exponencial de todos los elementos del array
array_reshape.exp()
#seno de todos los elementos del array
array_reshape.sin()
#coseno de todos los elementos del array
array_reshape.cos()
#tangente de todos los elementos del array
array_reshape.tan()
#ordenar el array
Array_reshape.sort()
#invertir el array
-np.sort(-array_reshape)
Array_reshape.reverse()
#transpuesta de la matriz
array_reshape.T
#dimensiones del array
array_reshape.shape
#numero de elementos del array
array_reshape.size
#tipo de datos del array
array_reshape.dtype
#numero de dimensiones del array
array_reshape.ndim
#numero de filas del array
array_reshape.shape[0]
#numero de columnas del array
array_reshape.shape[1]

#seleccion de varios elementos de array_reshape
array_reshape[0,0]
#nos dice si los valores son menores a 2 con true o false
array_reshape<2
#nos dice los valores menores a 2
array_reshape[array_reshape<2]

print(numeros_primos_array)
print(Array_zeros)
print(Array_unos)
print(Array_unos_enteros)
print(Array_rango)
print(Array_rango_pasos)
print(Array_rango_decimales)
print(Array_unos_enteros)