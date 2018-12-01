# 1) Examen
import numpy as np
import pandas as pd
from scipy import misc
import matplotlib.pyplot as plt
## 2) Crear un vector de ceros de tamaño 10
vector_ceros = np.zeros(10)

## 3) Crear un vector de ceros de tamaño 10 y el de la posicion 5 sea igual a 1
vector_ceros_2 =np.zeros(10)
vector_ceros_2[5]=1

## 4) Cambiar el orden de un vector de 50 elementos, el de la posicion 1 es el de la 50 etc.
vector_cincuenta = np.random.rand(50)
vector_cincuenta = vector_cincuenta[::-1]

## 5) Crear una matriz de 3 x 3 con valores del cero al 8
matriz_1 = np.array(range(9))
matriz_1 = matriz_1.reshape(3,3)

## 6) Encontrar los indices que no sean cero en un arreglo
arreglo = [1,2,0,0,4,0]
np.where(arreglo != 0)

## 7) Crear una matriz de identidad 3 x 3 
matriz_identidad = np.identity((3))

## 8) Crear una matriz 3 x 3 x 3 con valores randomicos
matriz_random = np.random.rand(3,3)

## 9) Crear una matriz 10 x 10 y encontrar el mayor y el menor
matriz_10x10 = np.random.rand(10,10)
matriz_10x10.max()
matriz_10x10.min()

## 10) Sacar los colores RGB unicos en una imagen (cuales rgb existen ej: 0, 0, 0 - 255,255,255 -> 2 colores)
mapache = misc.face()
mapache.size
mapache.item(0,0,0)
mapache.item(255,255,255)


## 11) ¿Como crear una serie de una lista, diccionario o arreglo?
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))
ser_mylist = pd.Series(mylist)
ser_myarr = pd.Series(myarr)
ser_mydict = pd.Series(mydict)

## 12) ¿Como convertir el indice de una serie en una columna de un DataFrame?
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))
ser = pd.Series(mydict)

df = pd.DataFrame(mylist,index = ser)
df1 = pd.DataFrame(myarr,index = ser)
#df2 = pd.DataFrame(mydict,index = ser)

# Transformar la serie en dataframe y hacer una columna indice
x = np.random.rand(26)
ser
df_x = pd.DataFrame(x,index=ser,columns = ["columna1"])
## 13) ¿Como combinar varias series para hacer un DataFrame?

import numpy as np
ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))

df_series = pd.DataFrame(dict(ser1 = ser1, ser2 = ser2))

## 14) ¿Como obtener los items que esten en una serie A y no en una serie B?

ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])
a = ser1.loc[ser2]

## 15) ¿Como obtener los items que no son comunes en una serie A y serie B?

ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])
ser1.diff()

## 16) ¿Como obtener el numero de veces que se repite un valor en una serie?

ser = pd.Series(np.take(list('abcdefgh'), np.random.randint(8, size=30)))
ser.value_counts()

## 17) ¿Como mantener los 2 valores mas repetidos de una serie, y a los demas valores cambiarles por 0 ?

np.random.RandomState(100)
ser = pd.Series(np.random.randint(1, 5, [12]))
ser_alt =  ser.value_counts()
ser_alt[2:] = 0
ser_alt

## 18) ¿Como transformar una serie de un arreglo de numpy a un DataFrame con un `shape` definido?

ser = pd.Series(np.random.randint(1, 10, 35))
ser.values.reshape(7,5)
df = pd.DataFrame(ser.values.reshape(7,5))


## 19) ¿Obtener los valores de una serie conociendo la posicion por indice?


ser = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
pos = (0, 4, 8, 14, 20)
ser.iloc()==pos
ser.loc[pos[0]]
ser.loc[pos[1]]
ser.loc[pos[2]]
ser.loc[pos[3]]
ser.loc[pos[4]]


# a e i o u


## 20) ¿Como anadir series vertical u horizontalmente a un DataFrame?

ser1 = pd.Series(range(5))
ser2 = pd.Series(list('abcde'))
df=pd.DataFrame(ser1)
##añadir columnas
df['ser2']=ser2
##añadir filas
df2 = pd.DataFrame(ser1)
df.append({9,'x'},ignore_index=True)
pd.concat([df,df2])

## 21)¿Obtener la media de una serie agrupada por otra serie?

#`groupby` tambien esta disponible en series.


frutas = pd.Series(np.random.choice(['manzana', 'banana', 'zanahoria'], 10))
frutas.columns=['frutas']
pesos = pd.Series(np.linspace(1, 10, 10))
print(pesos.tolist())
print(frutas.tolist())

frutas[[0]]
pesos.groupby(['0'])

#> [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
#> ['banana', 'carrot', 'apple', 'carrot', 'carrot', 'apple', 'banana', 'carrot', 'apple', 'carrot']

# Los valores van a cambiar por ser random
# apple     6.0
# banana    4.0
# carrot    5.8
# dtype: float64

#```


## 22)¿Como importar solo columnas especificas de un archivo csv?

constructors =  pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv",usecols=['age'])

https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv.





