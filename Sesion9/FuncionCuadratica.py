## Actividad: Función Cuadrática
# - Crea una función en la cual recibas como argumentos los parámetros de una función cuadrática, y te regrese x1 y x2.

import numpy as np

def FuncCuadratica(a,b,c):
    disc=b**2-4*a*c

    if disc>0:
        x_1=(-b+np.sqrt(disc))/(2*a)
        x_2=(-b-np.sqrt(disc))/(2*a)
        print("La ecuación tiene dos raíces reales distintas:\nx_1={0}\nx_2={1}".format(x_1,x_2)) 
    elif disc==0:
        x_1=-b/(2*1)
        print("La ecuación tiene una raíz real de multiplicidad doble:\nx_1=x_2={0}".format(x_1))
    else:
        re=-b/(2*a)
        im=np.sqrt(-disc)/(2*a)
        print("La ecuación tiene dos raíces complejas:\nx_1={0}+i{1}\nx_2={0}-i{1}".format(re,im))

print("Ingresa los parámetros de la función cuadrática:")
inparams=["a","b","c"]
params=[]
for i in inparams:
    params.append(float(input(i+": ")))

FuncCuadratica(params[0],params[1],params[2])