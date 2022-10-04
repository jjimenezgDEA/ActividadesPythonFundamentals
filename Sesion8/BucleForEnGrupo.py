## Actividad: Bucle for en grupo
# - Cada compañero dirá un número. Los guardarás en un diccionario, junto con el nombre de tu pareja.
# - Luego imprimirán los valores del diccionario (nombre de la persona y número que dijo) (Usando un bucle for)
# - Al final imprimirán dos mensajes, mostrando el número más grande, y el número más pequeño que dijeron, sin el nombre del socio, sólo el número.

# Lista de compañeros
compañeros=["Ivan","Hiram","Josue","Carlos","Pao","Sofi","Fer"]
diccionario=dict.fromkeys(compañeros)
for k in compañeros:
    diccionario[k]=float(input(k+", di un número: "))
print("\n")
for k,v in diccionario.items():
    print(k+" dijo el número "+str(v))
print("\n")10
print("El número más grande es: ",max(diccionario.values()))
print("El número más pequeño es: ",min(diccionario.values()))

