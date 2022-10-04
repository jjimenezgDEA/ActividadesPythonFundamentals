## Actividad: Competidores Olímpicos
# - Crear un programa en Visual Studio que me permita saber cuál es el competidor más veterano que ha recibido medalla (oro, plata o bronce)
# - Crear un programa en Visual Studio que me permita saber cuál es el competidor más joven que ha recibido medalla de oro
# - Encuentra al competidor más ganador de la historia y crea un csv con toda su información.

import pandas as pd
datos=pd.read_csv("C:/Users/JJIMENEZG/Documents/Python Fundamentals/Actividades/Sesion10/athlete_events.csv")
datosMedallista=datos[datos["Medal"].notna()]
medallistaYear=datosMedallista[datosMedallista["Year"].notna()].sort_values(by=["Year"])

medallistaOro=datos[datos["Medal"]=="Gold"]
oroEdad=medallistaOro[medallistaOro["Age"].notna()].sort_values(by=["Age"])

masGanador=datos["Name"].value_counts().index[0]
masGanador_df=datos[datos["Name"]==masGanador]
masGanador_df.to_csv("C:/Users/JJIMENEZG/Documents/Python Fundamentals/Actividades/Sesion10/CompetidorMasGanador.csv",header=True,index=True)

print("El competidor más veterano que ha recibido medalla es: ",medallistaYear.iloc[0].Name)
print("El competidor más joven que ha recibido medalla de oro es: ",oroEdad.iloc[0].Age)